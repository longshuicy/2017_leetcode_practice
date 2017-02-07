class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # decide it's one or two
        # then decide how many
        S = [1,2,2]
        idx = 2
        while len(S) < n:
            S += S[idx] * [(3 - S[-1])]
            idx += 1
        return S[:n].count(1)

if __name__ =='__main__':
    test = Solution()
    print(test.magicalString(6))
