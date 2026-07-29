class Solution:
    def profit(self,nums):
        buy_price = nums[0]
        profit = 0
        for price in nums:
            if price < buy_price:
                buy_price = price
        profit = max(profit, price - buy_price)
        return profit

prices = [7,6,4,3,1]
s1 = Solution()
print(s1.profit(prices))