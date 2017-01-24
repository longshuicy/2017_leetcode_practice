class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        s = sorted(s)
        g = sorted(g)
        count = 0
        
        for kid in g:
            for cookie in s:
                if kid <= cookie:
                    count += 1
                    s.remove(cookie)
                    break
                
                #print(count)
        
        return count


if __name__ == '__main__':

    test = Solution()
    test.findContentChildren([1,2,3],[1,2])
