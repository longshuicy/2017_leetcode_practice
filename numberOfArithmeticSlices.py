class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = sum = 0
        
        for i in range(1,len(A)-1):
            if A[i]-A[i-1] == A[i+1]-A[i]:
                
                count += 1 # every time move forward one means a new array itself, and one new combine with previous one
                sum += count
            else:
                count = 0
                
        return sum

if __name__ == '__main__':

    test = Solution()
    print(test.numberOfArithmeticSlices([1,3,5,6,7,9,11,13]))
