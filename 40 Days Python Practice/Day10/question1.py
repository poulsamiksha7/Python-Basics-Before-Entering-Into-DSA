#  Star pyramid

n=int(input("Enter Number: "))
for i in range(0,n):
    for j in range(n-i):
        print("*",end=" ")
    print()