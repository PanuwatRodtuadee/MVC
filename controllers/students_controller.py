from models.students import get_all_students, get_student_by_id
def show_all_students():
    return get_all_students()

def show_student_profile(student_id):
    return get_student_by_id(student_id)