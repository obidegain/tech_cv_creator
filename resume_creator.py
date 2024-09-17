from pylatex import Command, Document, Section, Subsection, Package, Center, LargeText, LineBreak, HugeText
from pylatex.utils import NoEscape, italic, bold


class ResumeCreator:

    def __init__(self):
        self.doc = self.set_conf_doc()
        self.personal_name = None

    @staticmethod
    def set_conf_doc() -> Document:
        doc = Document(documentclass="article", document_options=["a4paper"])
        doc.packages.append(Package(name="geometry", options="margin=1in"))
        doc.packages.append(Package(name="titlesec"))  # Añadir el paquete titlesec

        # Ajustar el espaciado antes del título de la sección (-0.5em es solo un ejemplo)
        doc.append(NoEscape(r'\titlespacing{\section}{0pt}{-0.5em}{1em}'))
        return doc

    def create_personal_information_section(self, personal_info: dict):
        """Add a centered section with personal information.

        This function creates a centered section in the document containing personal information
        such as name, email, telephone number, and place of residence.

        :param personal_info: A dictionary containing the personal information.
                              It should include the following keys:
                              - 'name' (str): Full name of the person.
                              - 'email' (str): Email address.
                              - 'tel' (str): Telephone number.
                              - 'place' (str): Location or place of residence.
        :type personal_info: dict
        """

        doc = self.doc
        with doc.create(Center()) as centered:
            name = personal_info.get('name')
            email = personal_info.get('email')
            tel = personal_info.get('tel')
            place = personal_info.get('place')
            space_text = " | "

            self.personal_name = name

            centered.append(LargeText(HugeText(bold(name))))
            centered.append(LineBreak())  # Salto de línea

            centered.append(email + space_text)
            centered.append(tel + space_text)
            centered.append(place)

    @staticmethod
    def create_right_line(right_text: str, bold: bool = True) -> str:
        if not bold:
            return right_text

        start_right_line = r'\textbf{'
        end_line = r'}'
        return start_right_line + right_text + end_line

    @staticmethod
    def create_left_line(left_text: str, with_enter: bool = True) -> str:
        start_left_line = r'\hfill{'
        end_line_with_enter = r'}\\'
        end_line = r'}'
        if not with_enter:
            return start_left_line + left_text + end_line
        return start_left_line + left_text + end_line_with_enter

    def create_line(self):
        doc = self.doc
        value = r'\vspace{-1.8em}'
        rule = r'\noindent\rule{16cm}{0.4pt}'
        enter_line = r'\\'
        doc.append(NoEscape(value))
        doc.append(NoEscape(rule))
        doc.append(NoEscape(enter_line))

    def create_full_line(self, right_text: str, left_text: str, bold: bool = True, with_enter: bool = True):
        doc = self.doc
        right_text_formated = self.create_right_line(right_text, bold)
        left_text_formated = self.create_left_line(left_text, with_enter)
        doc.append(NoEscape(right_text_formated))
        doc.append(NoEscape(left_text_formated))

    def create_work_experience_section(self, jobs: list[dict]):
        """Add a section with jobs details.

        This function creates a section in the document containing details for each job
        such as job title, company name, dates period, and place and type of job.

        :param jobs: A list of dictionaries that each one containing the job details.
                              Each job dict should include the following keys:
                              - 'job_title' (str): Full name of position.
                              - 'company_name' (str): Full name of company.
                              - 'dates' (str): Period of your experience. i.e "Jan. 2021 - Mar. 2023"
                              - 'place_and_type' (str): Location or place of and type of job. i.e "Remote for CDMX".
        :type jobs: list[dict]
        """

        doc = self.doc
        with doc.create(Section("WORK EXPERIENCE", numbering=False)):
            enter_line = r'\\'
            self.create_line()
            for i, job in enumerate(jobs):
                job_title = job.get('job_title', '')
                company_name = job.get('company_name', '')
                dates = job.get('dates', '')
                place_and_type = job.get('place_and_type', '')
                tasks = job.get('tasks', [])
                tools = job.get('tools', None)
                methodology = job.get('methodology', None)
                with_enter = True

                if i == len(jobs):
                    with_enter = False

                self.create_full_line(job_title, dates)
                self.create_full_line(company_name, place_and_type, with_enter=with_enter)

                for task in tasks:
                    task_text = "- " + task + enter_line
                    doc.append(NoEscape(task_text))

                if tools and methodology:
                    doc.append(NoEscape(enter_line))
                    doc.append("Tools: " + tools)
                    doc.append(NoEscape(enter_line))
                    doc.append("Methodology: " + methodology)
                    doc.append(NoEscape(enter_line))

                doc.append(NoEscape(enter_line))


    def create_education_section(self, educations: list[dict]):
        doc = self.doc
        with doc.create(Section("EDUCATION", numbering=False)):
            self.create_line()
            for i, education in enumerate(educations):
                name = education.get('name')
                dates = education.get('dates')
                institute = education.get('institute')
                place = education.get('place')
                with_enter = True

                if i == len(educations):
                    with_enter = False

                self.create_full_line(name, dates)
                self.create_full_line(institute, place, bold=False, with_enter=with_enter)


    def create_certifications_section(self, certifications: list):
        doc = self.doc
        with doc.create(Section("CERTIFICATIONS", numbering=False)):
            self.create_line()
            for i, certification in enumerate(certifications):
                title = certification.get('title')
                dates = certification.get('dates')
                with_enter = True

                if i == len(certifications):
                    with_enter = False

                self.create_full_line(title, dates, with_enter=with_enter)

    def create_languages_section(self, languages: list[dict]):
        doc = self.doc
        with doc.create(Section("LANGUAGES", numbering=False)):
            self.create_line()
            for i, language in enumerate(languages):
                name = language.get('name')
                level = language.get('level')
                with_enter = True

                if i == len(languages):
                    with_enter = False

                self.create_full_line(name, level, with_enter=with_enter)

    def create_about_me_section(self, about_me: str):
        doc = self.doc
        with doc.create(Section("ABOUT ME", numbering=False)):
            self.create_line()
            doc.append(about_me)

    def generate_pdf(self, file_name: str = None):
        doc = self.doc
        if not file_name:
            file_name = f'Resume - {self.personal_name}'
        doc.generate_pdf(file_name, clean_tex=False)
