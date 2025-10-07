# Question 3: Loops and Pattern Printing (15 points)

# Create a right triangle pattern using nested loops:

# **Input:** Number of rows (n)

# **Pattern for n=4:**
# ```
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# ```

# **Hint:** Use nested for loops

num=int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()