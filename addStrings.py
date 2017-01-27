class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        
        # '123' +　'45'
        i = len(num1)-1
        j = len(num2)-1
        carry = 0
        summation = []
        
        while i>=0 or j>=0:
            if i>=0 and j>=0:
                sum = carry + int(num1[i]) + int(num2[j])
            elif i>=0:
                sum = carry + int(num1[i])
            else:
                sum = carry + int(num2[j])
                
            if sum >9:
                digit = sum-10
                carry = 1
            else:
                digit = sum
                carry = 0
                
            summation.insert(0,str(digit))
            i -= 1
            j -= 1
        
        if carry == 1:
            summation.insert(0,str(carry))
        
        return ''.join(summation)

if __name__ == '__main__':
    test= Solution()
    print(test.addStrings('9','1'))
