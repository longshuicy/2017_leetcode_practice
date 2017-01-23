class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #print(bin(num)[2:])
        binary = bin(num)[2:]
        flipped = ''
        for i in binary:
            if i == '1':
                flipped += '0'
            elif i == '0':
                flipped += '1'
                
        #print(int(flipped,2))
        
        return int(flipped,2)


if __name__ == "__main__":
    test = Solution()
    print(test.findComplement(5))
