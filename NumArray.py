class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # slow
        return sum(self.dp[i:j+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

class NumArray2(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = nums
        # to save some time [a0, a0+a1, a0+a1+a2, a0+a1+a2+a3,...]
        
        for i in range(1,len(self.dp)):
            self.dp[i] += self.dp[i-1]
            #print(self.dp)
        
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # slow
        #return sum(self.dp[i:j+1])
        
        if i == 0:
            # print(self.dp[j])
            return self.dp[j]
        else:
            return sum(self.dp[j]-self.dp[i-1])

if __name__ == "__main__":

    test = NumArray2([-2,0,3,-5,2,-1])
    print(test.sumRange(2,5))


