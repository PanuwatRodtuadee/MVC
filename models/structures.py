from config import db
structures = db["subject_structures"]
def add_structure(data):
    structures.insert_one(data)

def get_structure_by_curriculum(curriculum_id):
    return structures.find_one({"curriculum_id": curriculum_id})