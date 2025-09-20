from flask import render_template
from controllers.students_controller import show_student_profile
from models.registration import get_registered_subjects

def student_profile_view(student_id):
    student = show_student_profile(student_id)
    subjects = get_registered_subjects(student_id)
    return render_template("student_profile.html", student=student, subjects=subjects)