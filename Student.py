students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        student = {
            "Roll": roll,
            "Name": name,
            "Marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for s in students:
                print("Roll:", s["Roll"], "| Name:", s["Name"], "| Marks:", s["Marks"])

    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        found = False

        for s in students:
            if s["Roll"] == roll:
                print("Student Found:")
                print("Roll:", s["Roll"])
                print("Name:", s["Name"])
                print("Marks:", s["Marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter Roll Number to delete: ")

        for s in students:
            if s["Roll"] == roll:
                students.remove(s)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")