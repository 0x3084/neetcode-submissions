from typing import  List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        for i in range(len(nums) -1):

            if  nums[i] == nums[i +1]:
                return True

        return False


m = Solution()

print(m.hasDuplicate( [3, 2, 3, 1]))
