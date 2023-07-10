
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#-n 快慢指针找中点
def end_of_first_half(self, head):
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow

#-n 两数之和 (链表版)
# https://leetcode.cn/problems/add-two-numbers/submissions/
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    p1,p2 = l1,l2
    dummy = ListNode(-1)
    p=dummy
    carry =0
    #! 固定三个东西 进位
    while p1!=None or p2!=None or carry>0:
        val = carry
        if p1!=None:
            val += p1.val
            p1=p1.next
        if p2!=None:
            val += p2.val
            p2=p2.next
        carry = val//10
        val = val%10
        p.next= ListNode(val)
        p=p.next
    return dummy.next

#-n 反转链表
def reverse(self, head: ListNode) -> ListNode:
    pre, cur = None, head
    while cur:
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node

#-n 合并两个有序链表
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    p = dummy
    p1 = l1
    p2 = l2

    while p1 and p2: 
        # 比较 p1 和 p2 两个指针
        # 将值较小的的节点接到 p 指针
        if p1.val > p2.val:
            p.next = p2
            p2 = p2.next
        else:
            p.next = p1
            p1 = p1.next
        # p 指针不断前进
        p = p.next

    if p1:
        p.next = p1

    if p2:
        p.next = p2

    return dummy.next


    def longestValidParentheses(self, s: str) -> int:
        # 定义一个栈，用于存放括号的位置
        stack = [-1]
        # 定义一个变量，用于存放最长的括号的长度
        max_len = 0
        # 定义一个变量，用于存放括号的位置
        flag = -1
        # 遍历字符串s
        for i in range(len(s)):
            # 如果当前字符是括号，则将其位置放入栈中
            if s[i] == '(':
                stack.append(i)
            # 如果当前字符是右括号，则从栈中弹出一个括号，并记录其位置
            else:
                stack.pop(-1)
                # 如果栈不为空，则将栈顶元素出栈，并记录其位置
                if len(stack):
                    # stack.pop(-1)
                    max_len = max(max_len, i - stack[-1])
                # 如果栈为空，则将当前元素放入栈中
                else:
                    # flag = i
                    stack.append(i)
        # 返回最长的括号的长度
        return max_len
    
#-n 合并k个有序链表
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    import heapq
    # 创建一个链表头节点，并将其初始值设置为0
    dummy = ListNode(0)
    # 创建一个指针，用于指向头节点
    p = dummy
    # 创建一个列表，用于存储每个链表的头节点
    head = []
    # 遍历每个链表
    for i in range(len(lists)):
        # 如果链表中存在节点，则将其存入列表
        if lists[i] :
            # 将列表中的元素添加到列表中
            heapq.heappush(head, (lists[i].val, i))
            # 将链表中的节点设置为下一个节点
            lists[i] = lists[i].next
    # 当列表中存在节点时，开始循环
    while head:
        # 获取列表中的最小值
        val, idx = heapq.heappop(head)
        # 将最小值添加到链表头节点的下一个节点中
        p.next = ListNode(val)
        # 将链表头节点设置为下一个节点
        p = p.next
        # 如果链表中存在节点，则将其存入列表
        if lists[idx]:
            # 将列表中的元素添加到列表中
            # 将列表中的元素添加到列表中
            heapq.heappush(head, (lists[idx].val, idx))
            # 将链表中的节点设置为下一个节点
            lists[idx] = lists[idx].next
    # 返回链表头节点
    return dummy.next

def count(val):
    zerosum=0
    while val:
        if val%10 == 0:
            zerosum+=1
            val=val//10
        else:
            break
    return val,zerosum

if __name__ =='__main__':
    lists = [[1,4,5],[1,3,4],[2,6]]
    # mergeKLists
    print(count(4))
    n=10
    choices = [x for x in reversed(range(1,n+1))]
    print(choices)