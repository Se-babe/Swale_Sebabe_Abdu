import json
import os

# File paths
STUDENTS_FILE = 'students.json'
COURSES_FILE = 'courses.json'
ENROLLMENTS_FILE = 'enrollments.json'

# Load data from files
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_enrollments():
    if os.path.exists(ENROLLMENTS_FILE):
        with open(ENROLLMENTS_FILE, 'r') as f:
            return json.load(f)
    return []

# Initialize data
students = load_data(STUDENTS_FILE)
courses = load_data(COURSES_FILE)
enrollments = load_enrollments()

def add_student():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    students[student_id] = student_name
    save_data(students, STUDENTS_FILE)
    print("Student added successfully!")

def add_course():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    courses[course_id] = course_name
    save_data(courses, COURSES_FILE)
    print("Course added successfully!")

def enroll_student():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    if student_id in students and course_id in courses:
        enrollments.append({'student_id': student_id, 'course_id': course_id})
        with open(ENROLLMENTS_FILE, 'w') as f:
            json.dump(enrollments, f, indent=4)
        print(f"{students[student_id]} enrolled in {courses[course_id]}")
    else:
        print("Invalid student or course ID!")

def display_students():
    print("\nList of Students:")
    if not students:
        print(" - No students found.")
    else:
        for sid, name in students.items():
            print(f" - ID: {sid}, Name: {name}")

def display_courses():
    print("\nList of Courses:")
    if not courses:
        print(" - No courses found.")
    else:
        for cid, name in courses.items():
            print(f" - ID: {cid}, Course: {name}")

def display_enrollments():
    print("\nEnrollments:")
    if not enrollments:
        print(" - No enrollments found.")
    else:
        for record in enrollments:
            student = students.get(record['student_id'], "Unknown Student")
            course = courses.get(record['course_id'], "Unknown Course")
            print(f" - {student} enrolled in {course}")

def main():
    while True:
        print("\nUniversity Management System")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student to Course")
        print("4. Display All Students")
        print("5. Display All Courses")
        print("6. Display Enrollments")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_course()
        elif choice == '3':
            enroll_student()
        elif choice == '4':
            display_students()
        elif choice == '5':
            display_courses()
        elif choice == '6':
            display_enrollments()
        elif choice == '7':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
