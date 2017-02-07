class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
            
        count = 0
        for i in range(len(timeSeries)-1):
            count += min(duration, timeSeries[i+1]-timeSeries[i])
        
        return count+duration

if __name__ == '__main__':
    test = Solution()
    print(test.findPoisonedDuration([1,2,4,5,10],2))
