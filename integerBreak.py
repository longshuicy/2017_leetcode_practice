def integerBreak(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 2:
        return 1
        # 2 = 1+1
            
    if n ==3:
        # 3 = 1+2
        return 2
    if n ==4:
        return 4
            
    multiply = 1
    while n>4:
        multiply *= 3
        n -= 3
        # break to as many 3 as possible
       
    return multiply*n

print(integerBreak(24))
