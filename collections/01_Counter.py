from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        a1 = Counter(s)
        a2 = Counter(t)
        print(a1.values(), a2.values())
        return a1.values() == a2.values()
