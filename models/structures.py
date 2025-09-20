from config import db

structures = db["subject_structure"]
def create_structure(data):
    structures.insert_one(data)