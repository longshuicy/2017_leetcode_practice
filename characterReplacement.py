import collections
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #freq = max(set(list(s)), key=list(s).count)
        #print(list(s).count())
        #print(Counter(list(s)).most_common()[0][1])
        # sliding window

        if not s:
            return 0
            
        res = lo = hi = 0
        counts = collections.Counter()
        
        for hi in range(len(s)):
            counts[s[hi]] += 1
            max_char_n = counts.most_common(1)[0][1]
            if hi - lo - max_char_n + 1 > k:
                counts[s[lo]] -= 1
                lo += 1
        
        return hi - lo + 1

if __name__ == '__main__':
    test = Solution()
    print(test.characterReplacement("AAAABA",1))
