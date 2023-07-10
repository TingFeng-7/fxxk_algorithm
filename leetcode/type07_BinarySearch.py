from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,r = 0 , len(letters)
        if ord(letters[-1]) - ord(target) < 1:
            return letters[0]
        while l<r:
            mid = l+(r-l)//2
            print(letters[mid])
            if ord(letters[mid])- ord(target) < 1:
                l = mid+1
            elif ord(letters[mid])- ord(target) >= 1: #收缩区间
                r = mid
        return letters[r]
    
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n+1
        while l + 1 < r:
            m = (l+r)//2
            if m*(m+1)/2 <= n:
                l = m
            else:
                r = m
        return l
