# factorial
def FactCheck(n):
    if n==0 or n==1:
        return 1
    return n*FactCheck(n-1)
n=int(input("Enter Number: "))
print(FactCheck(n))