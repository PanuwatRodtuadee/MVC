from flask import Flask, render_template, request, redirect
from controllers.check_controller import login
from views.students_profile import student_profile_view
from views.admin_dashboard import admin_dashboard_view
from views.subject_registration import subject_registration_view
from views.grade_entry import grade_entry_view

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        role = login(request.form["username"], request.form["password"])
        if role == "admin":
            return redirect("/admin")
        elif role == "student":
            return redirect(f"/student/{request.form['username']}")
        else:
            return "เข้าสู่ระบบไม่สำเร็จ"
    return render_template("login.html")

@app.route("/admin")
def admin():
    return admin_dashboard_view()

@app.route("/student/<student_id>")
def student(student_id):
    return student_profile_view(student_id)

@app.route("/register/<student_id>")
def register(student_id):
    return subject_registration_view(student_id)

@app.route("/grade")
def grade():
    return grade_entry_view()

if __name__ == "__main__":
    app.run(debug=True)
