# Q3: Sum of even numbers only (1–100)
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print(sum)