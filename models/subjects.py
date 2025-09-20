from models.config import db

subjects = db["subjects"]
def create_subject(data):
    subjects.insert_one(data)