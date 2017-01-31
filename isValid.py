class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s[0] != '(' and s[0] != '[' and s[0] != '{' or len(s)==1:
            return False
        
        i = 0
        stack = []
        dict = {'(':')', '{':'}', '[':']'}
        
        for p in s:
            
            if p in dict.keys():
                stack.append(p)
            elif p in dict.values():
                if stack!=[] and dict[stack[-1]] == p:
                    stack.pop()
                else:
                    return False
            
        #print(stack)
        if stack == []:
            return True
        else:
            return False
                
                    
if __name__ == '__main__':

    test = Solution()
    print(test.isValid('()[]{[{}]}'))
