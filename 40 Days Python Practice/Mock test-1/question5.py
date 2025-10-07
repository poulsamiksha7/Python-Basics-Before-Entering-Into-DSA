# Question 5: Comprehensive Problem (20 points)

# Create a simple grade calculator:
# - Input: Student name and 5 subject marks
# - Calculate total and percentage
# - Assign grade based on percentage:
#   - 90-100: A+
#   - 80-89: A
#   - 70-79: B
#   - 60-69: C
#   - Below 60: F
# - Print: Name, Total, Percentage, Grade

# **Sample Input:** Name: Priya, Marks: 85, 92, 78, 88, 90  
# **Sample Output:** Priya - Total: 433, Percentage: 86.6%, Grade: A

student_name=input("Enter Student's Name: ")
mark1=int(input("Enter Marks of Science: "))
mark2=int(input("Enter Marks of Math: "))
mark3=int(input("Enter Marks of Geography: "))
mark4=int(input("Enter Marks of English: "))
mark5=int(input("Enter Marks of History: "))
marks=mark1,mark2,mark3,mark4,mark5
print(student_name)
sum=mark1+mark2+mark3+mark4+mark5
print(f"Total {sum}")

percentage= sum/500*100
print(f"Percentage {percentage}%")

if percentage >= 90:
    print("Grade A+")
elif percentage >= 80:
    print("Grade A")
elif percentage >= 70:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
else:
    print("Grade F")

