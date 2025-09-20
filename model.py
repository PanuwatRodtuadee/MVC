from pymongo import MongoClient
from config import db

client = MongoClient("mongodb://localhost:27017/")
db = client["student_database"]

class students():
    students = db["students"]
    def create_student(data):
        students.insert_one(data)
class subjects():
    subjects = db["subjects"]
    def create_subject(data):
        subjects.insert_one(data)
class structures():
    structures = db["subject_structure"]
    def create_structure(data):
        structures.insert_one(data)
class register():
    registrations = db["registered_subjects"]
    def register_subject(data):
        registrations.insert_one(data)
