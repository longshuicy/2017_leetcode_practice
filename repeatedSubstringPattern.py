class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        
        for i in range(2,len(str)+1):
            if len(str)%i ==0:
                #print(i)
                #print(str[:int(len(str)/i)]*i)
                composed_str = str[0:int(len(str)/i)]*i
                
                if composed_str == str:
                    return True
        
        return False

if __name__ == '__main__':

    test = Solution()
    print(test.repeatedSubstringPattern("abcdeabcdeabcde"))

