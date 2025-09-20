from flask import render_template, request, redirect
from models.registration import get_registered_subjects
from controllers.grade_controller import enter_grade

def grade_entry_view():
    if request.method == "POST":
        student_id = request.form["student_id"]
        subject_id = request.form["subject_id"]
        grade = request.form["grade"]
        enter_grade(student_id, subject_id, grade)
        return redirect("/grade")
    student_id = request.args.get("student_id")
    subjects = get_registered_subjects(student_id) if student_id else []
    return render_template("grade_entry.html", subjects=subjects, student_id=student_id)