import os
import openai
from dotenv import load_dotenv


class IJDAssistant:
    def __init__(self, additional_info, job_description, model_name="gpt-3.5-turbo"):
        load_dotenv()
        #additional_info = self.load_text("interactive-JD/data/bushel_data.txt")
        #job_description = self.load_text("interactive-JD/data/bushel_JD.txt")
        print(os.environ)
        self.client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        self.model_name = model_name
        self.messages = [{"role": "system",
                          "content":
                              "You are an assistant that provides information about job descriptions, given the job "
                              "description itself and additional information not seen by the job seeker."},
                         {"role": "user",
                          "content":
                              f"Company information:\n{additional_info}\nJob description:\n{job_description}"
                          }
                         ]

    def ask_question(self, question):
        """
        Sends a series of messages to OpenAI API and returns the complete response.
        """
        self.messages.append({"role": "user",
                              "content": f"Answer only this question to the best of your knowledge: {question}"})

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.messages,
            max_tokens=1024
        )
        # Assuming the API returns a completed response that can be read immediately:
        if response and response.choices:
            return response.choices[0].message.content
        return "No response from AI."

def load_text(file_path):
    """
    Load text from a specified file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


# Usage example
if __name__ == "__main__":

    additional_info = load_text("C:\\Users\\NDSU-Prof\\Documents\\GitHub\\Kompletion-AI\\interactive-JD\\data"
                                          "\\bushel_data.txt")
    job_description = load_text("C:\\Users\\NDSU-Prof\\Documents\\GitHub\\Kompletion-AI\\interactive-JD\\data"
                                          "\\bushel_JD.txt")
    assistant = IJDAssistant(additional_info, job_description)

    while True:
        question = input("\n\nAsk a question about the job: ")
        stream = assistant.ask_question(question)

        print(stream)
