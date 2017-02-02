class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
            
        i =j = 0
        carry = 0
        new = []
        
        while i <len(a) or j < len(b) or carry == 1:
            
            if len(a)-i-1>=0:
                a_digits = int(a[len(a)-i-1])
                i += 1
            else:
                a_digits = 0
                
            if len(b)-j-1>=0:
                b_digits = int(b[len(b)-j-1])
                j += 1
            else:
                b_digits = 0
            
            if a_digits + b_digits + carry >1:
                new.insert(0, str(a_digits + b_digits + carry-2))
                carry = 1
            else:
                new.insert(0, str(a_digits + b_digits + carry))
                carry = 0
            
            #print(new)
                
        
        return ''.join(new)

if __name__ == '__main__':

    test = Solution()
    print(test.addBinary('111','11'))
