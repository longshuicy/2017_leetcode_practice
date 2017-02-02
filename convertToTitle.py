import string
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        alphabet = {}
        i = 0
        for letter in string.ascii_uppercase:
            alphabet[i] = letter
            i += 1
            
        title = []
        
        while n >= 1:
            if n%26 == 0:
                title.insert(0,alphabet[25])
            else:
                title.insert(0,alphabet[n%26-1])
            
            n = int((n-1)/26)
            #print(n)
            
        #print(title)
        return "".join(title)

if __name__ == '__main__':

    test = Solution()
    print(test.convertToTitle(3520))
