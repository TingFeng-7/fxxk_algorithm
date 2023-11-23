from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity # 记录key-value的顺序 既要有顺序 也要有直接映射
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1     # 返回-1表示查找失败
        self.cache.move_to_end(key)  # 将当前访问的节点移到双向链表尾部
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value   # 修改key对应的value值
            self.cache.move_to_end(key)  # 将当前访问的节点移到双向链表尾部
            return

        if len(self.cache) >= self.cap: # 双向链表头部为最久没有被访问的节点，删除该节点
            self.cache.popitem(last=False)
            
        self.cache[key] = value #添加新节点到链表尾部

# @ java version
# @ import java.util.LinkedHashMap;
# import java.util.Map;

# class LRUCache {
#     private int capacity;
# @    private LinkedHashMap<Integer, Integer> cache;

#     public LRUCache(int capacity) {
#         this.capacity = capacity;
#         // 使用LinkedHashMap来保持插入顺序
# @        this.cache = new LinkedHashMap<>(capacity, 0.75f, true);
#     }

#     public int get(int key) {
#         // 如果缓存中没有该key，返回-1
#         return cache.containsKey(key) ? cache.get(key) : -1;
#     }

#     public void put(int key, int value) {
#         // 如果缓存中已经有了该key，更新其值并将其移到最后（表示最近使用）
#         if (cache.containsKey(key)) {
#             cache.put(key, value);
#         } else {
#             // 如果缓存满了，删除最久未使用的元素
#             if (cache.size() >= capacity) {
#                 Map.Entry<Integer, Integer> eldestEntry = cache.entrySet().iterator().next();
#                 cache.remove(eldestEntry.getKey());
#             }
#             // 插入新元素到缓存中，并将其移到最后
#             cache.put(key, value);
#         }
#     }
# }
