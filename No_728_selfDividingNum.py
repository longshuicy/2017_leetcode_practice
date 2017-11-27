class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def self_dividing(n):
            for d in str(n):
                if d == '0' or n % int(d) > 0:
                    return False
            return True
        
        output = []
        for number in range(left, right +1):
            if self_dividing(number):
                output.append(number)
        return output
