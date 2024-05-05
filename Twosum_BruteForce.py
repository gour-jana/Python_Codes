#Brute force approach
from typing import List
nums0 = [2,7,11,15]
target0 = 9
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums)
        for p1 in range(ln - 1):
            for p2 in range(p1 + 1, ln):
                if nums[p1] + nums[p2] == target:
                    return print([p1, p2])
        return []  

x = Solution()
x.twoSum(nums0,target0)

