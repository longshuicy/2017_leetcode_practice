class Solution:
    def defangIPaddr(self, address: str) -> str:

        return address.replace(".", "[.]")

if __name__ == "__main__":
    solution = Solution()
    solution.defangIPaddr("1.1.1.1")