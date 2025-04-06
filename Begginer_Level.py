# Student Grade Calculator
# Input: Name, roll number, marks in 5 subjects.
# Output: Total, average, and grade (A/B/C/Fail).
# Bonus: Store multiple students’ data using a list of dictionaries.

class Solution:
    def calculate_grade(self, avg):
        if avg >= 90:
            return 'A'
        elif avg >= 75:
            return 'B'
        elif avg >= 60:
            return 'C'
        else:
            return 'Fail'

# Create an instance of Solution class
sol = Solution()

students = []
num_students = int(input("Enter number of students: "))

for i in range(num_students):
    print(f"\nEnter details for student {i + 1}")
    name = input("Name: ")
    roll_no = input("Roll Number: ")

    marks = []
    for j in range(5):
        mark = float(input(f"Enter marks for subject {j + 1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5
    grade = sol.calculate_grade(average)

    student = {
        'Name': name,
        'Roll No': roll_no,
        'Marks': marks,
        'Total': total,
        'Average': average,
        'Grade': grade
    }

    students.append(student)

# Display Results
print("\n--- Student Results ---")
for student in students:
    print(f"\nName       : {student['Name']}")
    print(f"Roll No    : {student['Roll No']}")
    print(f"Marks      : {student['Marks']}")
    print(f"Total      : {student['Total']}")
    print(f"Average    : {student['Average']:.2f}")
    print(f"Grade      : {student['Grade']}")

        
