class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask
        
        # Om a är negativt i 32-bitars (högsta biten är 1)
        if a > 0x7FFFFFFF:
            return ~(a ^ mask)
        else:
            return a


s = Solution()
print(s.getSum(1, 1))  # Output: 2
print(s.getSum(-2, 3)) # Output: 1
