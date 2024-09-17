from resume_creator import ResumeCreator

if __name__ == "__main__":

    personal_info = {
        'name': "Octavio Bidegain",
        'email': "octa.bidegain@gmail.com",
        'tel': "+54 9 2262 339461",
        'place': "Buenos Aires, Argentina."
    }

    first_job = {
        'job_title': "Software Engineer",
        'company_name': "Kigüi",
        'dates': "Jan. 2023 – Present",
        'place_and_type': "Remote for CDMX, México",
        'tasks': [
            "Developed a data lake based on AWS.",
            "Managed pipelines using Glue, Athena, QuickSight, and Power BI, writing queries on Spark and SQL.",
            "Led a back-office team of 6 people.",
            "Developed an OCR system using AWS Textract and AWS Expense.",
            "Managed the backend based on Django.",
            "Deployed Docker containers to support the server migration from Heroku to AWS."
        ],
        'tools': "Python, Django, AWS, SQL, Docker, Github, Linux",
        'methodology': 'Agile'
    }
    second_job = {
        'job_title': "Project Engineer",
        'company_name': "Kigüi",
        'dates': "Jan. 2021 - Jan. 2023",
        'place_and_type': "Buenos Aires, Argentina",
        'tasks': [
            "Back-end development using Django.",
            "Developed web scraping solutions using Python libraries (Selenium, Requests, BeautifulSoup).",
            "Implemented machine learning for text analysis with Python (Sklearn).",
            "Gathered, structured, and made large volumes of data available using Python, AWS, SQL, Power BI.",
            "Developed and built IoT devices with hardware design and PCB construction using Arduino and 2G/3G/4G modules."
        ],
        'tools': "Python, Django, AWS, Github, Arduino",
        'methodology': 'Agile'
    }
    third_job = {
        'job_title': "Head of Departament",
        'company_name': "Edenor SA",
        'dates': "Jun. 2018 – Jan. 2022",
        'place_and_type': "Buenos Aires, Argentina",
        'tasks': [
            "Led a team of 70 people, ensuring tasks were completed with safety, quality, and efficiency.",
            "Managed and controlled the annual CAPEX and OPEX budget.",
            "Controlled and approved contractor certifications."
        ],
        'tools': None,
        'methodology': None
    }

    first_education = {
        'name': "MSc in Finance - Stock Markets",
        'dates': "Dec. 2022",
        'institute': "UCEMA (University of CEMA)",
        'place': "Buenos Aires, Argentina"
    }
    second_education = {
        'name': "Electromechanical Engineer",
        'dates': "Dec. 2018",
        'institute': "UNMDP (National University of Mar del Plata)",
        'place': "Buenos Aires, Argentina"
    }

    first_certification = {
        'title': "Full Stack Python Diploma, Government of Buenos Aires",
        'dates': "Aug. 2022",
    }

    second_certification = {
        'title': "Stock Markets Diploma, UCEMA",
        'dates': "Dec. 2020",
    }

    first_language = {
        'name': 'Spanish',
        'level': 'Native'
    }
    second_language = {
        'name': 'English',
        'level': 'Upper-intermediate'
    }

    jobs = [first_job, second_job, third_job]
    educations = [first_education, second_education]
    languages = [first_language, second_language]
    certifications = [first_certification, second_certification]

    resume = ResumeCreator()
    resume.create_personal_information_section(personal_info)
    resume.create_work_experience_section(jobs)
    resume.create_education_section(educations)
    resume.create_certifications_section(certifications)
    resume.create_languages_section(languages)
    resume.generate_pdf()
