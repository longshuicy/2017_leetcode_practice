from string import ascii_uppercase

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = {}
        i = 1
        
        for c in ascii_uppercase:
            alphabet[c] = i
            i += 1
            
        #print(alphabet)
        
        sum = 0
        for index, char in enumerate(s):
            sum += alphabet[char]*26**(len(s)-index-1)
        # print(sum)
        
        return sum
        
        # "26" instead of 10 or binary or hex


if __name__ == '__main__':
    s = 'ABC'
    test = Solution()
    print(test.titleToNumber(s))
