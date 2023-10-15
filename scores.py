# Asking user for the score
score = int(input("Enter your score: "))

# Determining grade based on the score
if 70 <= score <= 100:
    grade = "A"
elif 60 <= score < 70:
    grade = "B"
elif 50 <= score < 60:
    grade = "C"
elif 40 <= score < 50:
    grade = "D"
elif 0 <= score < 40:
    grade = "Fail"
else:
    grade = "Invalid score"

# Printing the grade
print("Your grade is:", grade)
