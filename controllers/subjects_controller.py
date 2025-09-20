from models.subjects import get_subjects_by_curriculum
def show_available_subjects(curriculum_id):
    return get_subjects_by_curriculum(curriculum_id)