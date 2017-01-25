class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        flag = False
        list_magazine = list(magazine)
        if ransomNote == "":
            return True
        else:
            for i in ransomNote:
                if i in list_magazine:
                    list_magazine.remove(i)
                    flag = True
                else:
                    flag = False
                    break
            
        return flag

if __name__ == '__main__':
    test = Solution()
    print(test.canConstruct("aa","aab"))
