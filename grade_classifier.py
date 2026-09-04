score = int(input("Enter score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score.")
elif score >= 80:
    grade = "A"
    print(f"Grade: {grade}")
elif score >= 70:
    grade = "B"
    print(f"Grade: {grade}")
elif score >= 60:
    grade = "C"
    print(f"Grade: {grade}")
elif score >= 50:
    grade = "D"
    print(f"Grade: {grade}")
else:
    grade = "F"
    print(f"Grade: {grade}")