from typing import List

#@ 参考资料
# https://leetcode.cn/problems/short-encoding-of-words/solutions/175331/python3-hou-zhui-shu-mo-ban-ti-820-dan-ci-de-ya-su/

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None
    
# https://leetcode.cn/problems/short-encoding-of-words/
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.Trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['#'] = 1

    def isTail(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.Trie
        for w in word:
            curr = curr[w]
        return len(curr) == 1
    
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        cnt = 0
        words = set(words)
        for word in words:
            trie.insert(word[::-1])
        for word in words:
            if trie.isTail(word[::-1]):
                cnt += len(word) + 1
        return cnt

#@ https://leetcode.cn/problems/replace-words/
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for d in dictionary:
            trie.insert(d)
        words = sentence.split(" ")
        return " ".join(trie.find_sp(word) for word in words)

class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        node = self.root
        for w in word + "#":
            if w not in node:
                node[w] = {}
            node = node[w]
    
    def find(self, word):
        node = self.root
        for i in range(len(word)):
            if "#" in node:
                if self.find(word[i:]):
                    return True
            if word[i] in node:
                node = node[word[i]]
            else:
                return False
        return "#" in node
    
    def find_sp(self, word: str) -> str:
        node = self.root
        for i in range(len(word)):
            if "#" in node:
                return word[:i]
            if word[i] in node:
                node = node[word[i]]
            else:
                break
        return word
