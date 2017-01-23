class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        length = 32
        count = 0
        a = '{0:032b}'.format(x)
        b = '{0:032b}'.format(y)
        for i in range(length):
            if a[i] != b[i]:
                count += 1
        
        return count

if __name__ == "__main__":
    test = Solution()
    print(test.hammingDistance(1,4))
