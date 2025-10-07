# Question 1: Variables and Input/Output (10 points)

# Write a program that:
# - Takes user's name and age as input
# - Calculates birth year (assume current year is 2025)
# - Prints: 'Hello [name], you were born in [year]'

# **Sample Input:** Name: Rahul, Age: 22  
# **Sample Output:** Hello Rahul, you were born in 2003

name=input("Enter your name: ")
age=int(input("Enter your age: "))
year=2025
birth_year=year-age
print(f"Hello {name}, you were born in {birth_year}")


# OR


from datetime import datetime
name=input("Enter your name: ")
age=int(input("Enter your age: "))
current_year = datetime.now().year
birth_year=current_year-age
print(f"Hello {name}, you were born in {birth_year}")

