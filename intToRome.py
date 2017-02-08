class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        M = ["", "M", "MM", "MMM"] #1000
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] #100
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] #10
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] #0-9
        
        return M[int(num/1000)] + C[int((num%1000)/100)] + X[int((num%100)/10)] + I[num%10]

if __name__ =='__main__':

    test = Solution()
    print(test.intToRoman(5))  
