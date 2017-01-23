class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
                
        start = 0
        end = len(s)-1
        
        while start < end:

            while s[start] not in vowel and start<end:
                start += 1
                
                
            while s[end] not in vowel and start<end:
                end -= 1
                
            
            temp = s[end]
            #print(temp)
            s[end] = s[start]
            s[start]=temp

            #print('s',start)
            #print('e',end)
            start +=1
            end -=1

            #print(s)
                
        return (''.join(s))


if __name__ == "__main__":
    test = Solution()
    print(test.reverseVowels('hello'))
