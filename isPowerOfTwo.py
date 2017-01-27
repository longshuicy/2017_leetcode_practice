class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #print(n)
        if n == 0:
            return False
        else:

            if n%2==0 and n!=1:
                return self.isPowerOfTwo(n/2)
            elif n==1:
                return True
            else:                
                return False
                
                
        #return True


if __name__ == '__main__':
    test= Solution()
    print(test.isPowerOfTwo(17))
