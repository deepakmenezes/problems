class Solution:

    # Chatgpt generated
    def romanToInt1(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = prev = roman_map[s[-1]]
        for char in s[-2::-1]:
            curr = roman_map[char]
            result += curr if curr >= prev else -curr
            prev = curr
        return result
    
    def romanToInt2(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total + roman[s[-1]]
