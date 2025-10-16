# Practice: Sum odd numbers (1–50)
sum=0
for i in range(1,51):
    if i%2!=0:
        sum+=i
print(sum)