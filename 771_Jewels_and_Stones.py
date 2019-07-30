class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        total_num = 0
        for gem in J:
            total_num += S.count(gem)

        return total_num

if __name__ == "__main__":

    solution = Solution()
    print(solution.numJewelsInStones("aA", "aAAbbbb"))