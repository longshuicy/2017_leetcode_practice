class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) == 0:
            return True
            
        sent = []
        for letter in s:
            if letter.isalnum():
                sent.append(letter.lower())
                
        #print(sent)
        
        start = 0
        end = len(sent)-1
        
        while start < end:
            
            if sent[start] == sent[end]:
                #print(sent[start],sent[end])
                start += 1
                end -= 1
            else:
                return False
                
        return True

if __name__ == "__main__":

    test = Solution()
    print(test.isPalindrome("A man, a plan, a canal: Panama"))
