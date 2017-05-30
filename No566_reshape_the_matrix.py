import numpy

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        shape = numpy.array(nums).shape
        
        if r*c != shape[0]*shape[1]:
            return nums
            
        else:
            return numpy.reshape(nums, (r, c)).tolist()

if __name__ =='__main__':
    test = Solution()
    print(test.matrixReshape([[1,2],[3,4]],r=1,c=4))
