class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #We can plant a flower if the left neighbor is 0 
        #(or we are on the left edge), AND the right 
        #neighbor is 0 (or we are on the right edge).
        
        for i, x in enumerate(flowerbed):
            if (not x and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):
                n -= 1 # planted one tree
                flowerbed[i] = 1
   
        return n <= 0
