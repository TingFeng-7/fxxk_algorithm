import torch, os
from torch.utils.data import Dataset
from torchvision import transforms
from torch import nn
from PIL import Image
import pandas as pd
from torchtext.data import Field, TabularDataset

class ClipDataset(Dataset):
    def __init__(self, image_folder, descriptions_file, transform=None, tokenizer=None):
        self.image_folder = image_folder
        self.descriptions = pd.read_csv(descriptions_file)
        self.transform = transform
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.descriptions)

    def __getitem__(self, idx):
        img_name = self.descriptions.iloc[idx, 0]
        img_path = os.path.join(self.image_folder, img_name)
        image = Image.open(img_path).convert('RGB')

        if self.transform:
            image = self.transform(image)

        description = self.descriptions.iloc[idx, 1]

        if self.tokenizer:
            description_tokens = self.tokenizer(description)
            description = ' '.join(description_tokens)

        return {'image': image, 'description': description}

class SimplifiedCLIP(nn.Module):
    def __init__(self, text_model, vision_model):
        super(SimplifiedCLIP, self).__init__()
        self.vision_model = vision_model
        self.text_model = text_model
        self.cosine_similarity = nn.CosineSimilarity(dim=1)

    def forward(self, images, texts):
        # Extract features from images and texts
        image_features = self.vision_model(images)
        text_features = self.text_model(texts)

        # Normalize features
        image_features = image_features / image_features.norm(dim=-1, keepdim=True)
        text_features = text_features / text_features.norm(dim=-1, keepdim=True)

        # Compute cosine similarity between image and text features
        similarity_scores = self.cosine_similarity(image_features, text_features)

        return similarity_scores

def cross_entropy(preds, targets, reduction='none'):
    log_softmax = nn.LogSoftmax(dim=-1)
    loss = (-targets * log_softmax(preds)).sum(1)
    if reduction == "none":
        return loss
    elif reduction == "mean":
        return loss.mean()

def contrastive_loss(image_embeddings, text_embeddings, temperature):
    
        # Calculating the Loss
        logits = (text_embeddings @ image_embeddings.T) / temperature
        images_similarity = image_embeddings @ image_embeddings.T
        texts_similarity = text_embeddings @ text_embeddings.T
        targets = F.softmax(
            (images_similarity + texts_similarity) / 2 * temperature, dim=-1
        )
        texts_loss = cross_entropy(logits, targets, reduction='none')
        images_loss = cross_entropy(logits.T, targets.T, reduction='none')
        loss =  (images_loss + texts_loss) / 2.0 # shape: (batch_size)

