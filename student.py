import os

# File to store student records
FILE_NAME = "students.txt"

# Student format: ID, Name, Age, Course

def add_student():
    with open(FILE_NAME, "a") as file:
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        course = input("Enter student course: ")
        file.write(f"{student_id},{name},{age},{course}\n")
        print("Student added successfully!\n")

def display_students():
    print("\n--- Student Records ---")
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()
            if not students:
                print("No records found.\n")
                return
            for student in students:
                sid, name, age, course = student.strip().split(",")
                print(f"ID: {sid} | Name: {name} | Age: {age} | Course: {course}")
    except FileNotFoundError:
        print("No student file found.\n")

def search_student():
    keyword = input("Enter student ID or name to search: ")
    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            if keyword in line:
                sid, name, age, course = line.strip().split(",")
                print(f"\nFound: ID: {sid}, Name: {name}, Age: {age}, Course: {course}\n")
                found = True
    if not found:
        print("Student not found.\n")

def update_student():
    student_id = input("Enter student ID to update: ")
    updated = False
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    with open(FILE_NAME, "w") as file:
        for line in lines:
            sid, name, age, course = line.strip().split(",")
            if sid == student_id:
                print("Enter new details:")
                name = input("Name: ")
                age = input("Age: ")
                course = input("Course: ")
                file.write(f"{sid},{name},{age},{course}\n")
                updated = True
            else:
                file.write(line)
    if updated:
        print("Student updated successfully!\n")
    else:
        print("Student ID not found.\n")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    deleted = False
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    with open(FILE_NAME, "w") as file:
        for line in lines:
            if student_id not in line:
                file.write(line)
            else:
                deleted = True
    if deleted:
        print("Student deleted successfully!\n")
    else:
        print("Student ID not found.\n")

def menu():
    while True:
        print("==== Student Management System ====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.\n")

# Run the menu
menu()
