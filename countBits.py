class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        # slow one
        if num == 0:
            return [0]
        
        else:
            digits = [0]
            offset = 1
            for index in range(1,num+1):
                if index/2 == offset:
                    offset *= 2
                digits.append(digits[index - offset]+1)
        
        return digits


if __name__ == '__main__':

    test = Solution()
    print(test.countBits(10))
