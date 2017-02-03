import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # works but too slow 
        '''if n == 0 or n ==1:
            return 0
        
        count = 0
        for i in range(2, n):
            
            prime = True
            a=2
            while i >= a :
                if i%a==0 and a!=i:
                    prime = False
                    break
                else:
                    a += 1
                    
            if prime is True:
                count += 1
                
        return count'''
        
        # Sieve of Eratosthenes algorithm
        
        if n < 3:
            return 0
    
        isPrime = [0,0] + [1] *(n-2)
       
        i = 2
        while i*i < n:
            if isPrime[i] == 1:
                j = i*i
                while j<n:
                    isPrime[j] = 0
                    j += i
            i+= 1
        
        #print(isPrime)     
        return sum(isPrime)
        
if __name__ == "__main__":

    test = Solution()
    print(test.countPrimes(48801))

