import collections
import operator
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        dct = collections.Counter(list(s))
        sorted_dct = sorted(dct.items(), key=operator.itemgetter(1), reverse = True)
        
        new_s = []
        for item in sorted_dct:
            #print(item[0]*item[1])
            new_s.append(item[0]*item[1])
        
        return "".join(new_s)

if __name__ == '__main__':
    test = Solution()
    print(test.frequencySort('keatonchen'))
