class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        bin_n = '{0:032b}'.format(n)
        for i in bin_n:
            if i == '1':
                count +=1
        
        return count

if __name__ == '__main__':

    test = Solution()
    print(test.hammingWeight(90))
