class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        result = []
        dist_sum = 9999
        
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    
                    if i+j < dist_sum:
                        result = [list1[i]]
                        dist_sum = i+j
                    elif i+j == dist_sum:
                        result.append(list1[i])
                    
        return result


if __name__ =='__main__':
    test= Solution();
    print(test.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"]))
