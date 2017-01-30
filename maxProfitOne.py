class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Kadane's algorithm
        sum = 0
        maximum = 0
        
        for i in range(len(prices)-1):
            sum += prices[i+1]-prices[i]
            
            if sum <0:
                sum = 0
                
            maximum = max(maximum,sum)
            print(sum,maximum)
                
        return maximum

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    test = Solution()
    test.maxProfit(prices)
