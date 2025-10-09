#Method 1 :
n=int(input("Enter Number: "))
for i in range(1,n+1):
    for j in range(n-i+1):
        print("*",end=" ")
    print()            

# OR
#Method2 
n=int(input("Enter Number: "))
for i in range(0,n):
    for j in range(n-i):
        print("*",end=" ")
    print()
    
# OR
#Method3 
n=int(input("Enter Number: "))
for i in range(1,n+1):
    for j in range(0,n-i+1):
        print("*",end=" ")
    print()


#BUT FOR ME METHOD 2 IS EASY

# Outer loop:i=0
# Inner Loop j=3 (n-i=3-0=3)
# But main twist is that inner loop will start to run from 0 to n-1. Here 3 is value that how many stars are going to print in loop.
# SO j=0,1,2
# Print= ***

# Outer loop:i=1
# Inner Loop j=2 (n-i=3-1=2) 
# But main twist is that inner loop will start to run from 0 to n-1 . Here 2 is value that how many stars are going to print in loop.
# SO j=0,1
# Print= **

# Outer loop:i=2
# Inner Loop j=2 (n-i=3-2=1) 
# But main twist is that inner loop will start to run from 0 to n-1 . Here 1 is value that how many stars are going to print in loop.
# SO j=0
# Print= *

