from operator import itemgetter

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            l = [len(st) for st in strs]
            val, idx = min((val, idx) for (idx, val) in enumerate(l))
            shortest_str = strs[idx]
            for i in range(len(shortest_str)):
                current_char = shortest_str[i]
                for j in range(len(strs)):
                    if strs[j][i] != current_char:
                        return strs[j][0:i]
                    
            return shortest_str
                    
