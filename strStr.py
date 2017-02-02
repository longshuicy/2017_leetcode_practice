class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # print(len(needle),len(haystack))
        
        if needle =="" and haystack == "":
            return 0
        if needle =="" and haystack != "":
            return 0
        if needle != "" and haystack == "":
            return -1
        if len(needle)> len(haystack):
            return -1
            
        for i in range(len(haystack)):
            
            if needle[0] == haystack[i]:
                #print("hey")
                #print(haystack[i:i+len(needle)])
                
                if needle == haystack[i:i+len(needle)]:
                    
                    return i
        
        return -1

if __name__ == '__main__':

    test = Solution()
    print(test.strStr("PowerPoint","Point"))
