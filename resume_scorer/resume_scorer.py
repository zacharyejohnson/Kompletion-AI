import openai
from PyPDF2 import PdfReader 

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        return reader.pages[0].extract_text()
    except Exception as e:
        return f"Failed to read PDF: {str(e)}"

def score_resume(resume1_path, resume2_path, job_description):
    resume_text1 = extract_text_from_pdf(resume1_path) if resume1_path.endswith('.pdf') else open(resume1_path, 'r').read()
    resume_text2 = extract_text_from_pdf(resume2_path) if resume2_path.endswith('.pdf') else open(resume2_path, 'r').read()

    prompt = f"You are a job matcher. I will give you a job description and 2 resumes and you will give them a score 1-100 and explain why and select the better candidate by name.Here is the rubric. 40 points for experience, 20 points for skills, 20 points for education, 20 points for misc  The job description is: {job_description}. The resume1 is: {resume_text1} The resume2 is: {resume_text2}"

    client = openai.OpenAI(api_key="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")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    resume1 = "Zach Johnson Resume 2024.pdf"
    resume2 = "Avtonom Martushev Resume 2023.pdf"
    job_description = "We are looking for a software engineer with 5 years of experience in Python and a degree in computer science."
    score = score_resume(resume1, resume2, job_description)
    print("Response")
    print("################################")
    print(f"Score: {score}")