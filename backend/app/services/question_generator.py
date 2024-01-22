import requests
import json

class QuestionGenerator:
    def __init__(self, api_key, interview):
        self.api_key = api_key
        self.interview = interview

    def generate_questions(self, interview):
        """
        Generate interview questions using OpenAI's GPT-based LLM.

        :param interview: An Interview object containing job description, resume, and company goals.
        :return: List of generated questions.
        """
        prompt = self.construct_prompt(interview)
        questions = self.query_gpt_model(prompt)
        return questions

    def construct_prompt(self, interview):
        """
        Construct a structured prompt from the interview object.

        :param interview: An Interview object.
        :return: A string prompt for the LLM.
        """
        prompt = (
            f"Job Description: {interview.job_description}\n"
            f"Resume Summary: {interview.resume_summary}\n"
            f"Company Goals: {interview.company_goals}\n\n"
            "Based on the above information, generate relevant interview questions:\n"
        )
        return prompt

    def query_gpt_model(self, prompt):
        """
        Query the GPT-based model with the constructed prompt.

        :param prompt: A string prompt for the LLM.
        :return: List of generated questions.
        """

        response = requests.post("https://api.openai.com/v1/engines/gpt-4/completions",
                                 headers={"Authorization": f"Bearer {self.api_key}"},
                                 json={"prompt": prompt, "max_tokens": 100})
        questions = json.loads(response.text)["choices"][0]["text"].split('\n')

        return questions

# Example usage
# if __name__ == "__main__":
#     api_key = "your-openai-api-key"
#     qg = QuestionGenerator(api_key)
#     interview = InterviewObject(job_description="Software Engineer", resume_summary="Experienced in Python and Java", company_goals="Innovate in technology")
#     generated_questions = qg.generate_questions(interview)
#     for question in generated_questions:
#         print(question)
