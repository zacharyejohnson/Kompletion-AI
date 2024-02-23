from flask import Flask, render_template, request
import openai
import pandas as pd
from PyPDF2 import PdfReader

app = Flask(__name__)

# Replace 'your_api_key_here' with your actual OpenAI API key
openai.api_key = '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'

jd_path = "interactive-JD\\data\\bushel_JD.txt"

def load_additional_info():
    """
    Load additional company information from a file.
    """
    with open('interactive-JD\\data\\bushel_data.txt', 'r') as file:
       
        return file.read()
    

    
def get_job_description_pdf_text(path_to_jd):
    text = ""

    try:
        # Open the PDF file
        reader = PdfReader(path_to_jd)
        # Extract text from the first page
        text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        return text
    except Exception as e:
        return {"error": f"Failed to read PDF: {str(e)}"}
    

def get_job_description_text(path_to_jd):
    with open(path_to_jd, 'r', encoding='utf-8', errors='replace') as file:
        return file.read()

    


def generate_response(question):
    """
    Generate a response to the user's question using both the question
    and automatically loaded additional information.
    """
    additional_info = load_additional_info()
    prompt = construct_prompt()
    
    client = openai.OpenAI(api_key="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")
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=
        [
        {"role": "system", "content": f"You are a chatbot for an interactive job description app.\
            Your purpose is to standby and answer questions the job seeker may have about the job description they are looking at as they submit them.\
            You have access to additional information the job seeker does not about the company. Here is the additional information they cannot see: {additional_info}, \
            and here is the actual job description text they can see: {get_job_description_text(jd_path)}"},
        {"role": "user", "content": question}
        ]  ,
        temperature=0,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=None  # You might need to set stop sequences depending on your prompt structure
        )
    

    return response.choices[0].message.content


def construct_prompt():
    prompt = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        response = generate_response(question)
        return render_template('index.html', response=response)
    return render_template('index.html', response=None)

if __name__ == '__main__':
    app.run(debug=True)
