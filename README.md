# tech_cv_creator

# Resume Generator

This project provides a Python script that generates a professional PDF resume using the LaTeX document preparation system. It includes a customizable template where you can add your personal details, work experience, education, certifications, and languages.

## Requirements

To run this project, you need the following dependencies:

- Python 3.x
- [pylatex](https://github.com/JelteF/PyLaTeX) library for generating LaTeX documents
- LaTeX distribution (for compiling the document)
- `latexmk` tool (for building the PDF)

### Installing Dependencies

Recommendation: create an virtual enviroment.

1. Install `pylatex`:
   ```bash
   pip install -r requirements.txt
   ```
### Modify your information

2. Modify the sections instances with your information in personal_info.py. It's important that you modify each specific list with the correct number of instances in create_list() in main.py. For example: if you have only 2 job experiences, you must modify the jobs list in main.py, the same with education, certification, languages.

### Run the script and create your resume

3. Run main.py:
   ```bash
   python3 main.py
   ```
4. If you didn't install latexmk you will have an error. Please, install the tool:
   ```bash
   sudo apt-get install latexmk
   ```

Your resume will be create in the same folder with the follow name: "Resume - {your_full_name}.py"
