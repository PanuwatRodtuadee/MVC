from config import db
def enter_grade(student_id, subject_id, grade):
    db["registered_subjects"].update_one(
        {"student_id": student_id, "subject_id": subject_id},
        {"$set": {"grade": grade}}
    )
