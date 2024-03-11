import gradio as gr
import openai
import os
import pandas as pd
from PyPDF2 import PdfReader 
import re 
import json

# Initialize OpenAI with your API Key
openai.api_key = os.getenv('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')

def parse_resume(resume_file, attributes):
    """
    Parses the resume file using ChatGPT based on selected attributes.

    Args:
    - resume_file: The uploaded resume file.
    - attributes: A list of attributes to extract from the resume.

    Returns:
    A dictionary with attributes and their values extracted from the resume.
    """
    # Ensure the PDF file is readable
    resume_text = ""

    try:
        # Open the PDF file
        reader = PdfReader(resume_file)
        # Extract text from the first page
        resume_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    except Exception as e:
        return {"error": f"Failed to read PDF: {str(e)}"}


    # Create the prompt for ChatGPT
    attributes_list = "[" + ', '.join(attributes) + "]"
    prompt = construct_prompt(attributes_list, resume_text)
    
    # Query OpenAI's ChatGPT with the prompt
    client = openai.OpenAI(api_key="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")
    try:
        # Adjusted call for the new OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
           messages=
           [
            {"role": "system", "content": "You are a resume parser."},
            {"role": "user", "content": prompt}
            ]  ,
            temperature=0,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=None  # You might need to set stop sequences depending on your prompt structure
        )

        # Parsing the response according to the new API response structure
        parsed_response = response.choices[0].message.content


        # Convert the parsed response to a dictionary (implement this logic based on your expected response format)
        parsed_output = parse_chatgpt_response(parsed_response, attributes)
    except Exception as e:
        parsed_output = {"error": f"Failed to parse response: {str(e)}"}

    return parsed_output

def parse_chatgpt_response(response_text, attributes):
    """
    Parses the text response from ChatGPT into a dictionary based on the specified attributes.

    Args:
    - response_text: The text response from ChatGPT.
    - attributes: A list of attributes that the user wants to extract from the resume.

    Returns:
    A dictionary with the specified attributes as keys and their parsed values.
    """
    # Initialize an empty dictionary to hold the parsed attributes
    parsed_attributes = json.loads(response_text)

    # for attribute in attributes:
    #     # Construct a regex pattern to capture the value after the attribute
    #     # Adjust the pattern based on how ChatGPT formats the response
    #     pattern = f"{attribute}\s*:\s*(.+)"
    #     match = re.search(pattern, response_text, re.IGNORECASE)

    #     if match:
    #         # Add the attribute and its value to the dictionary
    #         parsed_attributes[attribute] = match.group(1).strip()

    return parsed_attributes



def construct_prompt(attributes_list, resume_text):

    prompt = f"You are a resume parser. Please search for and display the following attributes in the format of a python dictionary for each attribute in the list of attributes selected by the client, given here: {attributes_list}. \n\nResume:\n{resume_text}"
    return prompt

# Define the attributes users can select
attributes = [
    "Name", "Email", "Phone Number", "Skills", "Education", "Experience", "HAS_EXPERIENCE_WITH_REACT",  "HAS_USED_SQL"
]

# Create the Gradio interface
# with gr.Blocks() as demo:
#     gr.Markdown("## Resume Parser")
#     with gr.Row():
#         resume_upload = gr.File(label="Upload your resume")
#         attributes_select = gr.CheckboxGroup(choices=attributes, label="Select attributes to extract", value=["Name", "Email"])
#     submit_button = gr.Button("Parse Resume")
#     output = gr.JSON(label="Parsed Resume")

#     resume_upload.change(fn=parse_resume, inputs=[resume_upload, attributes_select], outputs=output)
#     submit_button.click(fn=parse_resume, inputs=[resume_upload, attributes_select], outputs=output)

if __name__ == "__main__":
    #demo.launch()

    response = parse_resume("Zach Johnson Resume 2024.pdf", attributes)

    print(response)

    for attr in attributes: 
        print("\n", attr, "\n", response[attr])
    