import collections
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dct =  [('zero',0),('two',2),('eight',8),('four',4),('one',1),('three',3),('five',5),('six',6),('seven',7),('nine',9)]
        # order matters
        ans = []
        S = collections.Counter(s)
        
        for key in dct:
            c = collections.Counter(key[0])
            while c&S==c:
                S -= c
                ans.append(key[1])
        
        #print(ans)
        
        return ''.join([str(i) for i in sorted(ans)])

if __name__ =='__main__':

    test = Solution()
    print(test.originalDigits("oetereirxnviuthwfosfoe"))   
