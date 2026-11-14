import json
try:
    with open("students.json", "r") as file:
        students = json.load(file)

except (FileNotFoundError, json.JSONDecodeError):
    students = {}

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Results")
    print("7. Exit")

    # Input Validation
    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Please enter a valid number!")
        continue

    print("Your choice:", choice)

    # 1. Add Student
    if choice == 1:

        name = input("Enter student name: ")

        try:
            mark = int(input("Enter student mark: "))
        except ValueError:
            print("Please enter a valid mark!")
            continue

        students[name] = mark

        with open("students.json", "w") as file:
            json.dump(students, file)

        print("Student added successfully!")
        print("Name:", name)
        print("Mark:", mark)

    # 2. View Students
    elif choice == 2:

        if not students:
            print("No students found!")

        else:
            for name, mark in students.items():
                print("Name:", name)
                print("Mark:", mark)

    # 3. Search Student
    elif choice == 3:

        name = input("Enter student name: ")

        if name in students:
            print("Name:", name)
            print("Mark:", students[name])

        else:
            print("Student not found!")

    # 4. Update Student
    elif choice == 4:

        name = input("Enter student name: ")

        if name in students:

            try:
                newmark = int(input("Enter new mark: "))
            except ValueError:
                print("Please enter a valid mark!")
                continue

            students[name] = newmark

            with open("students.json", "w") as file:
                json.dump(students, file)

            print("Student updated successfully!")

        else:
            print("Student not found!")

    # 5. Delete Student
    elif choice == 5:

        name = input("Enter student name: ")

        if name in students:

            students.pop(name)

            with open("students.json", "w") as file:
                json.dump(students, file)

            print("Student deleted successfully!")

        else:
            print("Student not found!")

    # 6. Calculate Results
    elif choice == 6:

        if not students:
            print("No students available!")

        else:
            total = sum(students.values())
            count = len(students)
            average = total / count

            print("Average marks:", average)

    # 7. Exit
    elif choice == 7:

        print("Thank you for using Student Management System!")
        break

    # Invalid menu option
    else:
        print("Invalid choice! Please select between 1 and 7.")