from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)

# --- File I/O ---
def load_json(file, default):
    return json.load(open(file)) if os.path.exists(file) else default

def save_json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

students = load_json("students.json", {})
courses = load_json("courses.json", {})
enrollments = load_json("enrollments.json", [])

# --- Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/students", methods=["GET", "POST"])
def manage_students():
    if request.method == "POST":
        sid = request.form["id"]
        name = request.form["name"]
        students[sid] = name
        save_json(students, "students.json")
        return redirect(url_for("manage_students"))
    return render_template("students.html", students=students)

@app.route("/courses", methods=["GET", "POST"])
def manage_courses():
    if request.method == "POST":
        cid = request.form["id"]
        cname = request.form["name"]
        courses[cid] = cname
        save_json(courses, "courses.json")
        return redirect(url_for("manage_courses"))
    return render_template("courses.html", courses=courses)

@app.route("/enroll", methods=["GET", "POST"])
def enroll():
    if request.method == "POST":
        sid = request.form["student_id"]
        cid = request.form["course_id"]
        if sid in students and cid in courses:
            enrollments.append({"student_id": sid, "course_id": cid})
            save_json(enrollments, "enrollments.json")
        return redirect(url_for("enroll"))
    return render_template("enrollments.html", enrollments=enrollments, students=students, courses=courses)

if __name__ == "__main__":
    app.run(debug=True)
