class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n%4 != 0:
            return True
        else:
            return False


if __name__ == "__main__":
    test = Solution()
    print(test.canWinNim(14))

# Liason's explanation is perfect
