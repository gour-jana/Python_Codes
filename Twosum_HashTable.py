#One pass hash table approach
from typing import List
nums0 = [2,8,11,15]
target0 = 9
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums)
        HashMap = {}  # creating empty hash table to map value to index

        for n1 in range(ln):
            complement = target - nums[n1]
            if complement in HashMap:
                return print([HashMap[complement],n1])
            HashMap[nums[n1]] = n1
        return print("No solution found")  

x = Solution()
x.twoSum(nums0,target0)

