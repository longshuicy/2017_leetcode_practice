class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # without recursive
        # return ((num-1)&num)==0 and (num-1)%3==0;
        
        # with loop:
        while num%4 == 0 and num!=0:
            num = num/4
            
        if num != 1:
            return False
        else:
            return True


if __name__ == '__main__':

    test = Solution()
    print(test.isPowerOfFour(4**5))
