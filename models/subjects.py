from config import db
subjects = db["subjects"]
def add_subject(data):
    subjects.insert_one(data)

def get_subjects_by_curriculum(curriculum_id):
    return list(subjects.find({"curriculum_id": curriculum_id}))