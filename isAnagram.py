import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if collections.Counter(s) == collections.Counter(t):
            return True
        else:
            return False


if __name__ == '__main__':
    test = Solution()
    print(test.isAnagram('abcdee','eabcde'))
