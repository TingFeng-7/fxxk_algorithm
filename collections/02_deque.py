from queue import Queue
from collections import deque
from typing import List  # 正常的队列

# -n 创建普通队列对象
q = Queue()
q.put(1)       # 队列尾部插入元素
q.put(2)
q.put(3)
print(q.queue)  # 查看队列中的所有元素
a = q.get()    # 返回并删除队列头部元素
print('take:', a)
print(q.queue)  # 运行结果deque([2,3])

# -n 创建双端队列对象
q1 = deque()
q1.append(1)  # 队列尾部插入元素
q1.append(3)
print(q1)  # 查看队列中的所有元素
a = q1.popleft()  # 返回并删除队列头部元素
print('take:', a)
print(q1)  # 运行结果deque([2,3])


class MaxQueue:
    def __init__(self):
        self.dq = deque()
        self.q = Queue()

    def max_value(self) -> int:
        return self.dq[0] if self.dq else -1

    def push_back(self, value: int) -> None:
        while self.dq and self.dq[-1] < value:
            self.dq.pop()
        self.dq.append(value)
        self.q.put(value)

    def pop_front(self) -> int:
        if not self.dq:
            return -1
        ans = self.q.get()
        if ans == self.dq[0]:
            self.dq.popleft()
        return ans

#~ 239. 滑动窗口最大值
import collections
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, 1 - k + n), range(n)):
            # 1. 删除 deque 中对应的 nums[i-1]
            print(i, j)
            if i > 0 and deque[0] == nums[i - 1]: # 最大值等于上一个左边界的时候
                deque.popleft()
            # 2. 保持 deque 非递减， 相同的如 33
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # 3. 记录窗口最大值
            if i >= 0: res.append(deque[0])
        return res
