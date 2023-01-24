from typing import List

class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        res = ""
        for a in zip(*strs):
            if len(set(a)) == 1: 
                res += a[0]
            else: 
                break
        return res

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:len(prefix) - 1]
        return prefix

Sol = Solution()
print(Sol.longestCommonPrefix1(['dee', 'deep', 'deepak']))
print(Sol.longestCommonPrefix2(['dee', 'deep', 'deepak']))
