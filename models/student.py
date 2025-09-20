from models.config import db

students = db["students"]
def create_student(data):
    students.insert_one(data)
