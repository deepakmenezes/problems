from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for a in zip(*strs):
            if len(set(a)) == 1: 
                res += a[0]
            else: 
                return res
        return res

Sol = Solution()
print(Sol.longestCommonPrefix(['dee', 'deep', 'deepak']))
