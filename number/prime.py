def findprime(n):
    res = []
    if n < 2:
        return None

    def isPrime(m):
        for i in range(2,m):
            if m%i == 0 and m!=i:
                return False
        return True

    for i in range (2,n+1):
        if isPrime(i):
            res.append(i)
    
    return res


print(findprime(122))