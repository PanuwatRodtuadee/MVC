from controllers.students_controller import show_student_profile
from models.registration import get_registered_subjects
def display_profile(student_id):
    student = show_student_profile(student_id)
    print(f"ชื่อ: {student['first_name']} {student['last_name']}")
    print("รายวิชาที่ลงทะเบียน:")
    for subject in get_registered_subjects(student_id):
        print(f"- {subject['subject_id']} เกรด: {subject['grade'] or 'ยังไม่ระบุ'}")