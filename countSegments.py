class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        # super ugly!!
        count = 0
        i = 0
        
        while i < len(s):
            
            if s[i] !=' ':
                
                j = i+1
                while j<len(s) and s[j]!=' ':
                    j += 1
                    
                i = j
                count += 1
            else:
                i += 1
        
        return count

    def countSegments2(self,s):
        # more concise solution
        count = 0
        for i in range(len(s)):

            if s[i]!=' ' and (i==0 or s[i-1] == ' '):
                count += 1

        return count

if __name__ == '__main__':

    test = Solution()
    print(test.countSegments(' a a a c a abcd egi sg , ,     ,'))
    print(test.countSegments2(' a a a c a abcd egi sg , ,     ,'))
