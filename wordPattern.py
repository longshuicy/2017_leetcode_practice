class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern = list(pattern)
        str = str.split(' ')
        
        if len(pattern) != len(str):
            return False
        
        dct= {}
        for i in range(len(pattern)):
            #print(dct)
            if pattern[i] not in dct.keys():
                if str[i] not in dct.values():
                    dct[pattern[i]]=str[i]
                else:
                    return False
            else:
                if dct[pattern[i]] != str[i]:
                    return False
                    
        return True

if __name__ == '__main__':

    test = Solution()
    print(test.wordPattern('abba','chen keaton keaton chen'))
