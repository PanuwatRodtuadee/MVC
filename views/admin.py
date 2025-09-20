from controllers.students_controller import show_all_students

def display_student_list():
    students = show_all_students()
    for s in students:
        print(f"{s['first_name']} {s['last_name']} - {s['school']}")