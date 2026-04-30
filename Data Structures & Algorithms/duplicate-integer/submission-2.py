from typing import  List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()


        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False



m = Solution()

print(m.hasDuplicate( [3, 2, 3, 1]))
