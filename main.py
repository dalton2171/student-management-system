# Student Management System

students = []


# Calculate grade
def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 35:
        return "D"
    else:
        return "E"


# Find student using admission number
def find_student(admission_no):
    for student in students:
        if student["admission_no"] == admission_no:
            return student

    return None


# Add a new student
def add_student():
    print("\n===== REGISTER STUDENT =====")

    admission_no = input("Admission No: ").strip().upper()

    if not admission_no:
        print("Admission number cannot be empty.")
        return

    # Check for duplicate admission number
    if find_student(admission_no) is not None:
        print("This admission number already exists!")
        return

    name = input("Student Name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    marks = []

    for subject in range(1, 4):
        while True:
            try:
                mark = float(
                    input(f"Enter Subject {subject} mark (0-100): ")
                )

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Mark must be between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    student = {
        "admission_no": admission_no,
        "name": name,
        "marks": marks
    }

    students.append(student)

    print(f"\nSuccess! {name} has been added.")


# Display one student's information
def display_student(student):
    marks = student["marks"]

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    print(
        f'{student["admission_no"]} | '
        f'{student["name"]} | '
        f'Marks={marks} | '
        f'Total={total:.1f} | '
        f'Avg={average:.1f} | '
        f'Grade={grade}'
    )


# List all students
def list_students():
    print("\n===== REGISTERED STUDENTS =====")

    if not students:
        print("No students registered yet.")
        return

    for student in students:
        display_student(student)


# Search for a student
def search_student():
    print("\n===== SEARCH STUDENT =====")

    admission_no = input(
        "Enter Admission No: "
    ).strip().upper()

    if not admission_no:
        print("Admission number cannot be empty.")
        return

    student = find_student(admission_no)

    if student is not None:
        print("\nStudent found:")
        display_student(student)
    else:
        print("No match found.")


# Display main menu
def show_menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("[1] Add Student")
    print("[2] List Students")
    print("[3] Search Student")
    print("[4] Exit")


# Main program
def main():
    while True:
        show_menu()

        choice = input("Choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            list_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-4.")


# Start program
if __name__ == "__main__":
    main()