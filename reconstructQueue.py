class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        '''Pick out tallest group of people and sort them in a subarray (S). 
        Since there's no other groups of people taller than them, 
        therefore each guy's index will be just as same as his k value.
        For 2nd tallest group (and the rest), insert each one of them into (S) by k value. 
        So on and so forth'''
        
        new_array = []
        
        while len(people)>0:
            max_h = -1
            max_ppl = []
            #print(people)
            for ppl in people:
                if ppl[0]> max_h:
                    max_h = ppl[0]
                    max_ppl = ppl
                elif ppl[0] == max_h:
                    #print(max_ppl,ppl)
                    
                    if ppl[1]<max_ppl[1]:
                        max_h = ppl[0]
                        max_ppl = ppl
                    
                    #print(max_ppl)
                
            
            new_array.insert(max_ppl[1],max_ppl)
            #print(new_array)
            #print(max_ppl)
            people.remove(max_ppl)
            
        return new_array

if __name__ == '__main__':
    test = Solution()
    print(test.reconstructQueue([[2,4],[3,4],[9,0],[0,6],[7,1],[6,0],[7,3],[2,5],[1,1],[8,0]]))
