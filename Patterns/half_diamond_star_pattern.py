n=int(input("Enter Number: "))
for i in range(2*n-1):
    stars=i
    if i<n:
        stars=i+1
    else:
        stars=2*n-1-i
    for j in range(stars):
        print("*",end="")
    print()

#n=3
#Outer Loop i=2*n-1 =5 
# i=0
#stars=i
# if statement True stars=i+1 =0+1=1 
# Inner Loop j=0 
# Print :*
#Outer Loop i=2*n-1 =5
# i=1
#stars=i
# if statement True(i<n) stars=i+1 =1+1=2
# Inner Loop j=0,1  
# Print **
#Outer Loop i=2*n-1 =5
# i=2
#stars=i
# if statement True stars=i+1 =2+1=3 
# Inner Loop j=0,1,2
# Print ***
#Outer Loop i=2*n-1 =5
# i=3
#stars=i
# if statement False stars=i+1
# Else Condition True Now stars=2*n-1-i = 2*3-1-3=2
# Inner Loop j=0,1 
# Print **
#Outer Loop i=2*n-1 =5
# i=4
#stars=i
# if statement False stars=i+1
# Else Condition True Now stars=2*n-1-i = 2*4-1-3=1
# Inner Loop j=0 
# Print *