from queue import Queue
from collections import deque # 正常的队列
# import queue

q = Queue()    #-n 创建普通队列对象
q.put(1)       # 队列尾部插入元素
q.put(2)
q.put(3)
print(q.queue) # 查看队列中的所有元素
a = q.get()    # 返回并删除队列头部元素
print('take:',a)
print(q.queue) # 运行结果deque([2,3])

q1 = deque()    #-n 创建双端队列对象
q1.append(1)       # 队列尾部插入元素
q1.append(2)
q1.append(3)
print(q1) # 查看队列中的所有元素
a = q1.popleft()    # 返回并删除队列头部元素
print('take:',a)
print(q1) # 运行结果deque([2,3])

class Maxq:

    def __init__(self):
        self.dq = deque()
        self.q = Queue()

    def max_value(self) -> int:
        #-n 左端就是最大值
        return self.dq[0] if self.dq else -1

    def push_back(self, value: int) -> None:
        #-n 
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

