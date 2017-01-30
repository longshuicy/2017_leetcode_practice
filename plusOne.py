class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ''' num = 0
        for i in range(len(digits)):
            num += digits[i]*(10**len(digits)-i-1)
            
        return num +1'''
        
        for i in range(len(digits)):
            if digits[len(digits)-1-i] <9:
                digits[len(digits)-1-i] = digits[len(digits)-1-i]+1
                return digits
            
            digits[len(digits)-1-i]=0
        
        digits.insert(0,1)
            
        return digits


if __name__ == '__main__':

    test = Solution()
    print(test.plusOne([9,9,9]))
