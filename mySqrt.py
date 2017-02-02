class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # 1+3+5+7 too slow
        
        if x<=0:
            return 0
        
        '''i = 1
        sum = 0
        count = 0
        while sum <= x:
            count += 1
            sum += i 
            i += 2
        
        return count -1'''
        
        '''r = x
        while r*r > x:
            
            r = (r + x/r) / 2
            
        return r'''
        
        r = x
        old = 0
        
        while abs(r - old) >1e-5:
            old = r
            r = r - (r**2 -x)/(2*r) 
            #print(old,r)
            
        return r

if __name__ == '__main__':

    test = Solution()
    print(test.mySqrt(11))
