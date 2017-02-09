class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        sorted_points = sorted(points, key = lambda x:x[1])
        #print(sorted_points)
        # shot at the end?
        if not points:
            return 0
            
        count = 1
        arrow = sorted_points[0][1]
        
        for ballon in sorted_points[1:]:
            if arrow<=ballon[1] and arrow>=ballon[0]:
                pass
            else:
                count += 1
                arrow = ballon[1]
            #print(arrow)
            #print(count)
        return count

if __name__ =='__main__':

    test = Solution()
    print(test.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))   
