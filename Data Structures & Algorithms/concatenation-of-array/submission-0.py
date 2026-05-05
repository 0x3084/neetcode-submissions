class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

    	ans =  [None] * len(nums) * 2

    	for m in range(len(nums)):
    		ans[m] = nums[m]
    		ans[m + len(nums)] =nums[m]
    	return ans

m = Solution()

print(m.getConcatenation([1,4,1,2]))
