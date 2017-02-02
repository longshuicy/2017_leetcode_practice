import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
        heaters = sorted(heaters)
        return max(min(abs(house - heater)
                   for i in [bisect.bisect(heaters, house)]
                   for heater in heaters[i-(i>0):i+1])
               for house in houses)


if __name__ == '__main__':

    test = Solution()
    print(test.findRadius([1,2,3,4],[1,4]))

    '''The idea is to leverage decent Arrays.binarySearch() function provided by Java.

For each house, find its position between those heaters (thus we need the heaters array to be sorted).
Calculate the distances between this house and left heater and right heater, get a MIN value of those two values. Corner cases are there is no left or right heater.
Get MAX value among distances in step 2. It's the answer.
Time complexity: max(O(nlogn), O(mlogn)) - m is the length of houses, n is the length of heaters.'''
