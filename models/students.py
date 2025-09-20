from config import db
students = db["students"]
def add_student(data):
    students.insert_one(data)
    
def get_all_students():
    return list(students.find())

def get_student_by_id(student_id):
    return students.find_one({"student_id": student_id})