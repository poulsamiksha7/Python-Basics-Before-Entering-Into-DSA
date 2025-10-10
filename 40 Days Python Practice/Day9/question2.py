# - Manual sort
l1=[1,3,2,5,4,6,7,9,8]
n=len(l1)
l2=[]
for i in range(1,n+1):
    for j in range(i+1,n):
        if i>j:
            l2.append(i)
    print(i)