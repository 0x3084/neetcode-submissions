class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        max_profit = 0

        for i in range(len(prices)):
            print(i)



            for k in range(i+1, len(prices)):


                
                profit =  prices[k] - prices[i]

                if profit > max_profit:
                        max_profit = profit
                        print(prices[k],"|",prices[i], 'profit:',profit, 'max_profit:', max_profit)

                        

        return max_profit


s = Solution()

print(s.maxProfit(prices = [10,1,5,6,7,1]))
        