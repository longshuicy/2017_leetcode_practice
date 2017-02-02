from collections import Counter
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        dct = {}
        
        for i in range(len(s)):
            #print(dct)
            if s[i] in dct.keys():
                if dct[s[i]] != t[i]:
                    return False
            elif t[i] in dct.values():
                
                for key in dct.keys():
                    if dct[key]==t[i]:
                        if key!=s[i]:
                            return False
            else:
                dct[s[i]]=t[i]
            
        return True

if __name__ =='__main__':
    test = Solution()
    print(test.isIsomorphic("ab","cc"))
