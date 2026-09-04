age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible.")
elif age >= 13:
    consent = input("Do you have consent? (yes/no): ").lower()

    if consent == "yes":
        print("You are eligible.")
    else:
        print("You are not eligible.")
else:
    print("You are not eligible.")