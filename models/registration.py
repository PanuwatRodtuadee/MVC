from config import db
registrations = db["registered_subjects"]
def register_subject(student_id, subject_id):
    registrations.insert_one({
        "student_id": student_id,
        "subject_id": subject_id,
        "grade": None
    })

def get_registered_subjects(student_id):
    return list(registrations.find({"student_id": student_id}))