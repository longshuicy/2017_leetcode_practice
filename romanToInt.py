class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabetic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        number = 0
        
        for index in range(len(s)-1):
            if alphabetic[s[index]]<alphabetic[s[index+1]]:
                number -= alphabetic[s[index]]
            else:
                number += alphabetic[s[index]]

        return number + alphabetic[s[-1]]

if __name__ == '__main__':
    test = Solution()
    print(test.romanToInt('LXXIII'))
