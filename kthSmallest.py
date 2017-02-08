class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # binary search:
        '''lo = matrix[0][0]
        hi = matrix[len(matrix)-1][len(matrix[0])-1]
        
        while(lo < hi):
            mid = lo + (hi - lo) / 2
            count = 0
            j = len(matrix[0]) - 1
            
            for i in range(len(matrix)):
                while(j >= 0 and matrix[i][j] > mid):
                    j-= 1
                    count += (j + 1)
            
            if(count < k):
                lo = mid + 1
            else:
                hi = mid
        
        return lo;'''
        flatten = []
        for row in matrix:
            for element in row:
                flatten.append(element)
        return sorted(flatten)[k-1]

if __name__ =='__main__':

    test = Solution()
    print(test.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))         
    
