#User function Template for python3

class Solution:
    def smithNum(self, n):
        # code here 
        return 1 if (sumDigits(n) == sumPrime(n) and isPrime(n) == 0 ) else 0 

def sumDigits(n):       
    #Find sum diggit
    sumDigits = 0
    while n > 0 :
        sumDigits += n%10
        n//=10    
    return sumDigits

def sumPrime(n):
    sumPrime = 0
    while n!=1 :
        i = 2
        while n%i != 0 :
            i += 1
        n//=i
        sumPrime += sumDigits(i)
    return sumPrime

def isPrime(n):
    if n <= 1 :
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0 :
            return 0
    return 1
