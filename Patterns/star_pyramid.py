n=int(input("Enter Number: "))
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(0,2*i+1):
        print("*",end="")
    print()

    
# n=3
# Outer Loop i=0
# Inner Loop j=3(n-i) (For Spaces)
# Second Inner Loop k=1 (2*1+1=1)
# Print= *

# Outer Loop i=1
# Inner Loop j=2(n-i) (For Spaces)
# Second Inner Loop k=3 (2*1+1=1)
# Print= ***

# Outer Loop i=2
# Inner Loop j=1(n-i) (For Spaces)
# Second Inner Loop k=5 (2*1+1=1)
# Print= *****