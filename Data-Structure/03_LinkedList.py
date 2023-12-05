from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @ 快慢指针找中点
def end_of_first_half(self, head):
    slow, fast = head, head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow

# @ 02. 两数相加 (链表版)
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    p1, p2 = l1, l2
    p = dummy = ListNode(-1)
    carry = 0
    #! 固定三个东西 进位
    while p1 != None or p2 != None or carry > 0:
        val = carry
        if p1 != None:
            val += p1.val
            p1 = p1.next
        if p2 != None:
            val += p2.val
            p2 = p2.next
        carry = val // 10
        val = val % 10
        p.next = ListNode(val)
        p = p.next
    return dummy.next

# @ 206 反转链表
def reverse_iter(head: ListNode) -> ListNode:
    pre, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre, cur = cur, nxt # 集体右移

# : 递归版本
# 定义：输入一个单链表头节点，将该链表反转，返回新的头结点
def reverse_recur(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    last = reverse_recur(head.next)  # (head.next) 先翻转
    head.next.next = head # (head.next).next 指向head  
    head.next = None  #  断开与后面部分的关系
    return last

# @ 92. 反转链表 II betwen
def reverseBetween( head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    p0 = dummy = ListNode(next=head)
    for _ in range(left - 1):
        p0 = p0.next #: P0 到达断点 前面

    pre = None
    cur = p0.next
    for _ in range(right - left + 1):
        nxt = cur.next #: 保存 nxt-node
        cur.next = pre  #: cur-node next 指向 pre-node
        pre = cur #: 两个指针右移
        cur = nxt

    p0.next.next = cur
    p0.next = pre
    return dummy.next

# @ 82. 删除排序链表中的重复元素 II
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = dummy = ListNode(next=head)
    while cur.next and cur.next.next:
        val = cur.next.val
        if cur.next.next.val == val:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next # 一直跳过，一直前进
        else:
            cur = cur.next
    return dummy.next

# @ 合并两个有序链表
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    p = dummy = ListNode(-1)  # ? P是实际遍历的，dummy是最后return的
    p1, p2 = l1, l2
    while p1 and p2:
        if p1.val > p2.val:  # ? 比较 p1 和 p2 两个指针 将值较小的的节点接到 p 指针
            p.next = p2
            p2 = p2.next
        else:
            p.next = p1
            p1 = p1.next
        p = p.next  # p指针不断前进

    if p1:
        p.next = p1
    if p2:
        p.next = p2
    return dummy.next

# @ 148. 排序链表 
def sortList(self, head: ListNode) -> ListNode:
    # : 给定链表头结点，请将其按升序排列并返回排序后的链表
    if not head or not head.next:
        return head  # termination.
    # cut the LinkedList at the mid index.
    slow, fast = head, head.next
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    mid, slow.next = slow.next, None  # save and cut.
    # recursive for cutting.
    left, right = self.sortList(head), self.sortList(mid)
    # merge `left` and `right` 两个有序链表
    h = res = ListNode(0)
    while left and right:
        if left.val < right.val:
            h.next, left = left, left.next
        else:
            h.next, right = right, right.next
        h = h.next
    h.next = left if left else right
    return res.next

# @143 重排链表
def reorderList(head):
    if not head or not head.next:
        return head
    # : 1.找到链表的中点
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # : 2.反转第二部分链表
    prev, current = None, slow.next
    slow.next = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    # : 3.合并两个链表
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2
    return head

def longestValidParentheses(self, s: str) -> int:
    stack = [-1] # 定义一个变量，用于存放最长的括号的长度
    max_len = 0 # 定义一个变量，用于存放括号的位置
    flag = -1 # 遍历字符串s
    for i in range(len(s)): # 如果当前字符是括号，则将其位置放入栈中
        if s[i] == '(':
            stack.append(i) # 如果当前字符是右括号，则从栈中弹出一个括号，并记录其位置
        else:
            stack.pop(-1) # 如果栈不为空，则将栈顶元素出栈，并记录其位置
            if len(stack):  # stack.pop(-1)
                max_len = max(max_len, i - stack[-1]) # 如果栈为空，则将当前元素放入栈中
            else:
                # flag = i
                stack.append(i)
    return max_len

# @ hard 合并K个有序链表
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    import heapq
    dummy = ListNode(0)    # 创建一个链表头节点，并将其初始值设置为0
    p = dummy     # 创建一个指针，用于指向头节点
    head = []     # 创建一个列表，用于存储每个链表的头节点
    # 遍历每个链表
    for i in range(len(lists)):
        if lists[i]:  # 如果链表中存在节点，则将其存入列表
            heapq.heappush(head, (lists[i].val, i))
            # 将列表中的元素添加到列表中
            lists[i] = lists[i].next            # 将链表中的节点设置为下一个节点

    while head:     # 当列表中存在节点时 , 获取列表中的最小值
        val, idx = heapq.heappop(head) # 将最小值添加到链表头节点的下一个节点中
        p.next = ListNode(val)
        # 将链表头节点设置为下一个节点
        p = p.next
        # 如果链表中存在节点，则将其存入列表
        if lists[idx]:
            # 将列表中的元素添加到列表中
            heapq.heappush(head, (lists[idx].val, idx))
            # 将链表中的节点设置为下一个节点
            lists[idx] = lists[idx].next
    # 返回链表头节点
    return dummy.next

# 旋转链表
def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return head
    length = 0
    cur = head
    while cur.next:
        cur = cur.next
        length += 1
    cur.next = head
    length += 1  # 计算链表长度
    k = k % length
    k = length - k  # 找到断点
    cnt = 0
    cur = head
    dummy = ListNode(None)
    while cur:
        cnt += 1
        if cnt == k:
            dummy = cur.next  # 存头节点
            cur.next = None  # 将断点变成尾部节点
            break
        cur = cur.next
    return dummy


def count(val):
    zerosum = 0
    while val:
        if val % 10 == 0:
            zerosum += 1
            val = val//10
        else:
            break
    return val, zerosum


if __name__ == '__main__':
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    # mergeKLists
    print(count(4))
    n = 10
    choices = [x for x in reversed(range(1, n+1))]
    print(choices)
