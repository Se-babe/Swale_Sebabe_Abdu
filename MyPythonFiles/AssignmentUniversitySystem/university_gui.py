import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os

# --- File handling ---
def load_data(file, default):
    return json.load(open(file)) if os.path.exists(file) else default

def save_data(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

students = load_data("students.json", {})
courses = load_data("courses.json", {})
enrollments = load_data("enrollments.json", [])

# --- Core Functions ---
def add_student():
    sid = simpledialog.askstring("Student ID", "Enter student ID:")
    name = simpledialog.askstring("Student Name", "Enter student name:")
    if sid and name:
        students[sid] = name
        save_data(students, "students.json")
        messagebox.showinfo("Success", "Student added!")

def add_course():
    cid = simpledialog.askstring("Course ID", "Enter course ID:")
    cname = simpledialog.askstring("Course Name", "Enter course name:")
    if cid and cname:
        courses[cid] = cname
        save_data(courses, "courses.json")
        messagebox.showinfo("Success", "Course added!")

def enroll_student():
    sid = simpledialog.askstring("Student ID", "Enter student ID:")
    cid = simpledialog.askstring("Course ID", "Enter course ID:")
    if sid in students and cid in courses:
        enrollments.append({'student_id': sid, 'course_id': cid})
        save_data(enrollments, "enrollments.json")
        messagebox.showinfo("Success", f"{students[sid]} enrolled in {courses[cid]}")
    else:
        messagebox.showerror("Error", "Invalid student or course ID.")

def show_data_window(title, data):
    win = tk.Toplevel(root)
    win.title(title)
    text = tk.Text(win, width=50, height=20)
    text.pack()
    for line in data:
        text.insert(tk.END, line + "\n")

def display_students():
    lines = [f"ID: {sid}, Name: {name}" for sid, name in students.items()]
    show_data_window("All Students", lines or ["No students found."])

def display_courses():
    lines = [f"ID: {cid}, Name: {name}" for cid, name in courses.items()]
    show_data_window("All Courses", lines or ["No courses found."])

def display_enrollments():
    lines = []
    for record in enrollments:
        sid = record['student_id']
        cid = record['course_id']
        sname = students.get(sid, "Unknown")
        cname = courses.get(cid, "Unknown")
        lines.append(f"{sname} enrolled in {cname}")
    show_data_window("Enrollments", lines or ["No enrollments found."])

# --- GUI Setup ---
root = tk.Tk()
root.title("University Management System")

tk.Label(root, text="University Management System", font=("Arial", 16)).pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Student", width=20, command=add_student).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Add Course", width=20, command=add_course).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Enroll Student", width=20, command=enroll_student).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="View Students", width=20, command=display_students).grid(row=1, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="View Courses", width=20, command=display_courses).grid(row=2, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="View Enrollments", width=20, command=display_enrollments).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=10)

root.mainloop()
