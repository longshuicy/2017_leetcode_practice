class Solution(object):
    
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
           
                
        if len(str(num)) ==1 :
            
            return num
            
        else:
            sum = 0
            for i in str(num):
                sum += int(i)
            #num = sum
            # print(num)
            
            return self.addDigits(sum)
            

if __name__ != '__main__':
    test = Solution()
    a = test.addDigits(38)
    print(a)
    
