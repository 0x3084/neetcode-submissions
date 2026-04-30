class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left = 0

        right = len(nums) -1

        while left <= right:
            mid = (left + right) // 2


            if nums[mid] == target:

                return int (mid)
            elif nums[mid] > target:

                right  = mid -1
            else:

                left = mid + 1

        return -1
s = Solution()
print(s.search(sorted([1, 3, 5, 7, 9, 12, 15]), target = 9))