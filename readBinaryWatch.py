class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        time = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    time.append('%d:%02d' % (h, m))
                
        return time


if __name__ == '__main__':
    test = Solution()
    print(test.readBinaryWatch(4))
