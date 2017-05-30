class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        pickN = len(candies)/2
        
        if len(set(candies))>=pickN:
            return pickN
        else:
            return len(set(candies))

if __name__ =='__main__':
    test= Solution();
    print(test.distributeCandies([1,1,2,2,3,3]))

