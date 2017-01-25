class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # find the maximum
        min_num = min(nums)
        
        moves = 0
        for num in nums:
            moves += num - min_num
            
        return moves


if __name__ == '__main__':
    test = Solution()
    a = [1,2,3]
    print(test.minMoves(a))
