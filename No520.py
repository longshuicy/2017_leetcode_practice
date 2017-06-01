class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        total = 0
        for c in word:
            total += c.isupper()
    
        return total == 0 or len(word) == total or (total == 1 and word[0].isupper())
