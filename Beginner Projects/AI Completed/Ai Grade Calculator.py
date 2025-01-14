# Grade Calculator
# Concept: Create a program that calculates a student's grade based on their scores in different subjects.
# Implementation:
# Create a list or dictionary to store subject names and corresponding scores.
# Calculate the average score.
# Determine the letter grade based on the average score (e.g., A, B, C, D, F).
# Print the calculated average and the letter grade.
# Learning Points:
# Data structures (lists or dictionaries)
# Loops (to iterate through scores)
# Conditional statements (to determine the letter grade)

subjects = {
    "Math": 85,
    "Science": 90,
    "English": 92,
    "History": 88,
    "Geography": 95
}

total_score = sum(subjects.values())

average_score = total_score / len(subjects)

letter_grade = ""

if average_score >= 90:
    letter_grade = "A"
    grade_description = "Excellent"
elif average_score >= 80:
    letter_grade = "B"
    grade_description = "Good"
elif average_score >= 70:
    letter_grade = "C"
    grade_description = "Satisfactory"
elif average_score >= 60:
    letter_grade = "D"
    grade_description = "Below Average"
else:
    letter_grade = "F"
    grade_description = "Failed"

print(f"Your average score is {average_score:.2f}.")

print(f"Your letter grade is {letter_grade}.")

print(f"Your grade description is {grade_description}.")