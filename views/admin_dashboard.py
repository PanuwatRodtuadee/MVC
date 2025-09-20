from flask import render_template
from controllers.students_controller import show_all_students

def admin_dashboard_view():
    students = show_all_students()
    return render_template("admin_dashboard.html", students=students)