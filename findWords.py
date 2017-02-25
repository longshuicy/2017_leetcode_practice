class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        row1 = ['q','w','e','r','t','y','u','i','o','p']
        row2 = ['a','s','d','f','g','h','j','k','l']
        row3 = ['z','x','c','v','b','n','m']
        
        output = []
        
        for word in words:
            if set(word.lower()).issubset(row1) or set(word.lower()).issubset(row2) or set(word.lower()).issubset(row3):
                output.append(word)
                
        return output


if __name__=='__main__':
    test = Solution()
    print(test.findWords(["Hello","Alaska","Dad","Peace"]))
