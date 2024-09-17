from venv import create

from resume_creator import ResumeCreator
from personal_info import *

def create_lists():
    # Modify with your specifics dependencies.
    jobs = [four_job, first_job, second_job, third_job]
    educations = [first_education, second_education]
    languages = [first_language, second_language]
    certifications = [first_certification, second_certification]

    return jobs, educations, languages, certifications

if __name__ == "__main__":

    jobs, educations, languages, certifications = create_lists()

    resume = ResumeCreator()
    resume.create_personal_information_section(personal_info)
    resume.create_work_experience_section(jobs)
    resume.create_education_section(educations)
    resume.create_certifications_section(certifications)
    resume.create_languages_section(languages)
    resume.generate_pdf()
