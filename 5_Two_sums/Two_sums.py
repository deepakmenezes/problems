
try:
    from typing import List
except ImportError:
    pass


class Solution:

    def twosums(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        print("ts2")
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in hashmap:
                return [i, hashmap[num2]]
            hashmap[nums[i]] = i

if __name__ == "__main__":
    output = Solution().twosums([-4, 2, 3, 4], 0)
    print(output)