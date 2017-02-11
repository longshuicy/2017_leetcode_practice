import collections
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        #Find a subset P of nums such that sum(P) = (target + sum(nums)) / 2
        
        count = collections.defaultdict(int)
        count[0] = 1
        
        for x in nums:
            step = collections.defaultdict(int)
            for y in count:
                #print(count[y],y+x,y-x)
                step[y + x] += count[y]
                #print(step[y-x])
                step[y - x] += count[y]
            count = step
            #print(step)
    
        return count[S]
        
        

if __name__ == '__main__':
    test = Solution()
    print(test.findTargetSumWays([1,2,3,4,5],3))
