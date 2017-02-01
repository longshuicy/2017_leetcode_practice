import string
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #if not s:
        #    return 0

        list_s = s.split(' ')

        print(list_s)

        for item in list_s:
            for i in range(len(item)):
                if item[i] not in string.ascii_letters:
                    del item[i]
        
        list_s = list(filter(None, list_s))

        print(list_s)

        if not list_s:
            return 0
        else:
            return len(list_s[-1])
        


if __name__ =='__main__':
    test = Solution()
    print(test.lengthOfLastWord(" "))
