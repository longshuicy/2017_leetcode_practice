import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        a word, phrase, or sequence that reads the same backward as forward
        """
        
        freq = collections.Counter(list(s))
        count = 0
        odd = 0
        
        for key in freq.keys():
            if freq[key]%2 != 0:
                odd += 1
        
        if odd == 0:
            return len(s)
        else:
            return len(s) - odd +1

if __name__ == '__main__':
    test = Solution()
    print(test.longestPalindrome('aabbccddde'))
