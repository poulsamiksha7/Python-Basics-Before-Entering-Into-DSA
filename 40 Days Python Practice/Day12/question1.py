#  Prime checker
def printChecker(n):
    if n<=1:
        return "The number is not prime"
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return "The number is not prime"
    return "The number is prime"
n=int(input("Enter Number: "))
print(printChecker(n))
         
    