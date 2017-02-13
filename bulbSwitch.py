import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 0
        
        while i**2 <=n:
            count += 1
            i += 1
                
        return count-1

if __name__ == '__main__':
    test = Solution()
    print(test.bulbSwitch(12))

'''I try explain my though as following:

How many "on" at the end of nth toggle?

--> "on" or "off" at each position in an array of length n?

--> toggle even number times will result in "on", toggle odd number times will result in "off"

--> for position k, the number of toggles is the number of distinct divisors that k has

--> divisors always come in pair, which means even number of divisors, for example, 12 has (1,12),(2,6),(3,4).

--> however, Square Number has odd number of divisors, e.g. 25 has 1,25,5

--> thus, the number of "on", is the number of perfect square number <= n
'''
