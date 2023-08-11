from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        # 缓存最大容量
        self.cap = capacity
        #! 记录key-value的顺序 既要有顺序 也要有直接映射
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            # 返回-1表示查找失败
            return -1
        self.cache.move_to_end(key) # 将当前访问的节点移到双向链表尾部
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 修改key对应的value值
            self.cache[key] = value
            self.cache.move_to_end(key) # 将当前访问的节点移到双向链表尾部
            return
        
        if len(self.cache) >= self.cap:
            # 双向链表头部为最久没有被访问的节点，删除该节点
            self.cache.popitem(last=False)

        # 添加新节点到链表尾部
        self.cache[key] = value
