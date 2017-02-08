import collections
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # four loops naive version
        '''count = 0
        for a in A:
            for b in B:
                 for c in C:
                     for d in D:
                         if a + b + c +d == 0:
                             count += 1
                             
        return count'''
        
        '''The naive solution is to run four loops by iterating all elements and check for (A[i] + B[j] + C[k] + d[h]) == 0. Time complexity: N^4
            We can improve solution by iterating through elements of three arrays and check if the fourth array contains A[i] + B[j] + C[k] + d == 0 ----> d = -A[i] - B[j] - C[k]. We can use HashSet to store elements of fourth array. Overall time complexity: N^3;
            To improve the solution we can divide arrays into two parts. Then make calculation of sums of one part (A[i] + B[j]) and store their sum's occurences counter in a HashMap. While calculating second part arrays' sum (secondSum = C[k] + D[h]) we can check whether map contains secondSum*(-1);
            A[i] + B[j] == - C[k] - D[h]
            A[i] + B[j] == - (C[k]+D[h])'''
            
        dct1 = collections.Counter(a+b for a in A for b in B)
        return sum(dct1[-c-d] for c in C for d in D)


if __name__ =='__main__':

    test = Solution()
    print(test.fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))
