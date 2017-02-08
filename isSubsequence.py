class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_iter = iter(t)
        return all(x in t_iter for x in s)


if __name__ =='__main__':

    test = Solution()
    print(test.isSubsequence("abc","aegljsgbjegjwc"))
