class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.cleanupinput(s)
        if s == s[::-1]:
            return True
        else:
            return False

    def cleanupinput(self, s: str) -> str:
        return ''.join([c for c in s if c.isalnum()]).lower()

sol = Solution()
print(sol.isPalindrome("abba"))