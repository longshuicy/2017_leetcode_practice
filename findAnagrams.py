import collections, time
class Solution(object):
    def findAnagrams1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        #int begin=0, end=0; //two pointers, one point to tail and one  head
        #int d; //the length of substrin

        #for() { /* initialize the hash map here */ }
        if len(s)<len(p):
            return []
            
        #hashmap = collections.Counter(p)
        index = []

        for i in range(len(s)-len(p)+1):
            #print(collections.Counter(s[i:i+len(p)]))
            #if collections.Counter(s[i:i+len(p)])==hashmap:
            copy = collections.Counter(p)
            flag = True
            
            for j in s[i:i+len(p)]:
                if j in copy.keys():
                    copy[j] -= 1
            
            for key in copy.keys():
                if copy[key] != 0:
                    flag = False
                    
            #print(copy)
            
            if flag == True:
                index.append(i)
        
        return index


    def findAnagrams2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        #int begin=0, end=0; //two pointers, one point to tail and one head
        #int d; //the length of substrin

        #for() { /* initialize the hash map here */ }
        if len(s)<len(p):
            return []
            
        hashmap = collections.Counter(p)
        index = []

        for i in range(len(s)-len(p)+1):
            #print(collections.Counter(s[i:i+len(p)]))
            if collections.Counter(s[i:i+len(p)])==hashmap:
                index.append(i)
        
        return index


    def findAnagrams3(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dct = collections.Counter(p)

        L, res, tmpdct = len(p), [], {}

        for i in range(len(s)-L+1):
            # updating is way faster than making a new dictionary
            
            if not tmpdct:                            # construct new temp dictionary
                for c in s[i:i+L]:
                    if c not in tmpdct: 
                        tmpdct[c] = 1
                    else: 
                        tmpdct[c] += 1
            
            else:                                     # update the dictionary
                tmpdct[s[i-1]] -= 1
                if s[i+L-1] in tmpdct: 
                    tmpdct[s[i+L-1]] += 1
                else: 
                    tmpdct[s[i+L-1]] = 1
            
            # tmpdct = collections.Counter(s[i:i+L])
                
            fit = True
            for k in dct.keys():
                if k not in tmpdct or dct[k] != tmpdct[k]:
                    fit = False
                    break
            if fit: res.append(i)
        
        return res
        


if __name__ =='__main__':
    s ="buqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdk\
    parxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyviz\
    lhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfy\
    vizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwg\
    fyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjenc\
    wgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjen\
    cwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjen\
    cwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencw\
    gfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfy\
    vizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfy\
    vizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgf\
    yvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwg\
    fyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencw\
    gfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjenc\
    wgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjen\
    cwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjen\
    cwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqt\
    jencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxoms\
    buqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparx\
    omsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkp\
    arxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhd\
    kparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizl\
    hdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvi\
    zlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfy\
    vizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwg\
    fyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjenc\
    wgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjen\
    cwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtje\
    ncwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtj\
    encwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqt\
    jencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuq\
    tjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqt\
    jencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuq\
    tjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbu\
    qtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsb\
    uqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxoms\
    buqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxom\
    sbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparx\
    omsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkpa\
    rxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdk\
    parxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlh\
    dkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyviz\
    lhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyv\
    izlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgf\
    yvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencw\
    gfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjen\
    cwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqt\
    jencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsb\
    uqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxo\
    msbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkpa\
    rxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhd\
    kparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyviz\
    lhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfy\
    vizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencw\
    gfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtje\
    ncwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuq\
    tjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxoms\
    buqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparx\
    omsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkp\
    arxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlh\
    dkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvi\
    zlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgf\
    yvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjenc\
    wgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtj\
    encwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbu\
    qtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxom\
    sbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkpar\
    xomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdk\
    parxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizl\
    hdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyv\
    izlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencw\
    gfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtj\
    kparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyvizlhdkparxomsbuqtjencwgfyviz"

    p ="ncwgfyvizlhdkparxoms"
    
    test = Solution()

    start1= time.time()
    print(test.findAnagrams1(s,p))
    end1 = time.time()
    print(end1-start1,'\n')

    start2= time.time()
    print(test.findAnagrams2(s,p))
    end2 = time.time()
    print(end2-start2,'\n')
    
    start3= time.time()
    print(test.findAnagrams3(s,p))
    end3 = time.time()
    print(end3-start3,'\n')
