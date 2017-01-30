class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return self.generate(1) + [[1,1]]
        
        lastLine = self.generate(numRows-1)[-1]
        newLine = [1]
        for i in range(len(lastLine)-1):
            newLine.append(lastLine[i]+lastLine[i+1])
        newLine.append(1)
        
        #print(newLine)
        
        return self.generate(numRows-1) + [newLine]

    def generate2(self,numRows):
        #iterative approach faster!
        trig = []
        if numRows == 0:
            trig =  []
        elif numRows == 1:
            trig =  [[1]]
        elif numRows == 2:
            trig = [[1],[1,1]]
        else:
            trig = [[1],[1,1]]
            for i in range(3,numRows+1):
                lastLine = trig[i-2]
                newLine = [1]
                for i in range(len(lastLine)-1):
                    newLine.append(lastLine[i]+lastLine[i+1])
                newLine.append(1)
                
                trig.append(newLine)
        
        #print(trig)
        return trig
            

if __name__ == '__main__':

    test = Solution()
    print(test.generate(25))
    print(test.generate2(25))
