class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        if rowIndex == 0:
            trig =  [1]
        elif rowIndex == 1:
            trig = [1,1]
        else:
            trig = [1,1]
            for i in range(rowIndex-1): # 
                trig.insert(0,1)
                #print(trig)
                
                for j in range(1,i+2):    # j = 0, 1, 2
                    trig[j] = trig[j]+trig[j+1]
                    #print(trig)
                    
        return trig


if __name__ == '__main__':

    test = Solution()
    print(test.getRow(5))
