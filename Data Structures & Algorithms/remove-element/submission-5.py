class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        
        for m in range(len(nums)):
            if nums[m] == val:
                continue
            else:
                nums[k] = nums[m]

                k += 1
        return k



i = Solution()

print(i.removeElement([1,1,2,3,4], val =1))