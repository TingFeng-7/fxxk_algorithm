from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    # 80. 删除有序数组中的重复项 II
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return n
        slow, fast = 2, 2
        while fast < n:
            if nums[slow-2] != nums[fast]:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        return slow
    
    # 82. 删除排序链表中的重复元素 II
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next