# Question 4: Lists and Data Processing (15 points)

# Given a list of numbers: `[12, 7, 23, 8, 19, 4, 15]`

# Write a program to:
# - Find and print all even numbers
# - Calculate and print the sum of odd numbers
# - Find the maximum number (without using max() function)

# **Expected Output:**
# ```
# Even numbers: [12, 8, 4]
# Sum of odd numbers: 64
# Maximum number: 23

num=[12,7,23,8,19,4,15]
new_list=[]
for i in num:
    if i%2==0:
        new_list.append(i)
print(f"Even Numbrs: {new_list}")

sum=0
for j in num:
    if j%2!=0:
        sum+=j
print(f"Sum of odd Numbers: {sum}")

max=0
for k in num:
    if k>=max:
        max=k
print(f"Maximum number: {max}")
