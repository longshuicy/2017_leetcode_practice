class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # too slow!
        
        count = 0
        for bin_num in zip(*map('{0:032b}'.format,nums)):
            # star unpack excellent!!
            #print(bin_num)
            count += bin_num.count('1')*bin_num.count('0')
                
        return count
        
        '''Total hamming distance for the i-th bit =
            (the number of zeros in the i-th position) *
            (the number of ones in the i-th position).'''

if __name__ =='__main__':
    test = Solution()
    print(test.totalHammingDistance([4,2,14]))
