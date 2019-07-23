class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        add = 0
        sum_array = []
        for i in range(len(nums)):
            add += nums[i]
            sum_array.append(add)
        
        if len(sum_array) == 1:
            return sum_array[0]
        else:
            max_num = sum_array[k-1]/k
            for j in range(len(sum_array)):
                if j+k < len(sum_array):
                    max_num = max(max_num, (sum_array[j+k] - sum_array[j])/k)

            return max_num        
                
