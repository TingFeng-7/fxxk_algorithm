import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    #~ 出现频率最高的TopK个字符串
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 字符串 -> 该字符串出现的频率
        wordToFreq = {}
        for word in words:
            wordToFreq[word] = wordToFreq.get(word, 0) + 1
        pq = []
        for word, freq in wordToFreq.items():
            # todo 存储负值，让小根堆变成大根堆
            pq.append((-freq, word))
        #! 构建小根堆, heappop弹出最小值
        heapq.heapify(pq)
        # 取出前k个高频单词
        res = []
        for _ in range(k):
            freq, word = heapq.heappop(pq)
            res.append(word)
        return res

    #~ 合并K个有序链表
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """_summary_

        Args:
            lists (List[ListNode]): N个链表的头结点

        Returns:
            ListNode: _description_
        """        
        import heapq
        dummy = ListNode(0)    # 创建一个链表头节点，并将其初始值设置为0
        p = dummy     # 创建一个指针，用于指向头节点
        res = []     # 创建一个列表，用于存储每个链表的头节点
    
        for i in range(len(lists)):
            if lists[i]:  # 如果链表中存在节点，则将其存入列表
                heapq.heappush(res, (lists[i].val, i))
                lists[i] = lists[i].next    # 已经进去了一个元素,将链表中的节点设置为下一个节点

        while res:  # 当列表中存在节点时
            # 获取列表中的最小值
            val, idx = heapq.heappop(res)
            # 将最小值添加到链表头节点的下一个节点中
            p.next = ListNode(val)
            p = p.next

            if lists[idx]:
                # 将列表中的元素添加到列表中
                heapq.heappush(res, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        # 返回链表头节点
        return dummy.next
