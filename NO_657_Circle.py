import collections

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        sequence = 'RLUD'
        
        if len(moves)%2 != 0:
            return False
        else:
            counter=collections.Counter(moves)
            if counter['U'] != counter['D'] or counter['L'] != counter['R']:
                return False
            else:
                return True
