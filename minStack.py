class MinStack(object):

    # too slow should save the minimum on the run
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        
        self.stack.insert(0,(x,curMin))


    def pop(self):
        """
        :rtype: void
        """
        return self.stack.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return None
        return self.stack[0][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return None
            
        return self.stack[0][1]
    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
