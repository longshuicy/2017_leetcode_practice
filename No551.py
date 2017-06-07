class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        a_count = 0
        l_count = 0
        for i in range(len(s)-1):
            if s[i] == 'A':
                a_count += 1
            if s[i] == 'L' and s[i+1] =='L':
                l_count += 1
            elif s[i] =='L' and s[i+1] !='L':
                l_count = 0
            
                
            if a_count >1 or (a_count==1 and s[i+1]=='A'):
                return False
            
            if l_count >1:
                return False
                
        return True
