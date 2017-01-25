import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # print(collections.Counter(list(s)))
        freq_dict = collections.Counter(list(s))
        for index, item in enumerate(s):
            if freq_dict[item] == 1:
                return index
                
        return -1
                

if __name__ == '__main__':
    s = 'iilovekeaton'
    test = Solution()
    print(test.firstUniqChar(s))
