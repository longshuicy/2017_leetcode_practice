class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        list_t = list(t)
        list_s = list(s)
        
        for i in list_s:
            if i in list_t:
                list_t.remove(i)
                
        return list_t[0]


if __name__ == '__main__':
    s = 'abcde'
    t = 'abcded'
    test = Solution()
    print(test.findTheDifference(s,t))
