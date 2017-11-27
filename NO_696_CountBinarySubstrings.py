class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        group = []
        count =  1
        
        # soooooo messssssssy!! 
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
                if i+1 == len(s)-1:
                    group.append(count)
            else:
                if i+1 == len(s)-1:
                    group.append(count)
                    group.append(1)
                else:
                    group.append(count)
                    count = 1
        print(group)
        
        output = 0
        for j in range(len(group)-1):
            output += min(group[j],group[j+1])
            
        return output
