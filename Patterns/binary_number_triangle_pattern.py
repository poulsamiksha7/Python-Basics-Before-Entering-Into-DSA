
n=int(input("Enter Your Number:" ))
start=1
for i in range(0,n):
    if i%2==0:
        start=1
    else:
        start=0
    for j in range(i+1):
        print(start,end=" ")
        start=1-start
    print()

# n=3 
# start=1
# Outer Loop:  i=0
# if i%2==0 start=1
# j=i+1 
# print =start = 1 -> 1

# start=1
# Outer Loop: i=1
# if 1%2!=0
# else: start=0
# j=1+1=2 0,1 
# print start= 0 1

# start=1
# Outer Loop: i=2
# if 2%2==0 start=1
# j=2+1=2 0,1 ,2
# print start= 1 0 1