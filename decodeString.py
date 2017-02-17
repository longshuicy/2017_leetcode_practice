class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        stack = [["",1]]
        num = ""
        
        for char in s:
            if char.isdigit():
                num += char
            elif char == "[":
                stack.append(["",int(num)])
                num = ""
            elif char == "]":
                string,k = stack.pop()
                stack[-1][0] += string*k
            elif char.isalpha():
                stack[-1][0] += char
                
            #print(stack)
        return stack[0][0]

if __name__ == '__main__':
    test = Solution()
    print(test.decodeString("32[a53[beg]]3[ag]"))
