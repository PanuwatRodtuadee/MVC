from flask import render_template, request, redirect
from controllers.subjects_controller import show_available_subjects
from models.registration import register_subject
def subject_registration_view(student_id):
    curriculum_id = "25650001"  
    if request.method == "POST":
        subject_id = request.form["subject_id"]
        register_subject(student_id, subject_id)
        return redirect(f"/student/{student_id}")
    subjects = show_available_subjects(curriculum_id)
    return render_template("subject_registration.html", subjects=subjects, student_id=student_id)
