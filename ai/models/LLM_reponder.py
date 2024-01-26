from openai import OpenAI


class OpenAIResponder:
    def __init__(self, interview):
        self.interview = interview
        




    def process_oai(self, transcription, memory, job_title, api_key="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"):

        client = OpenAI(api_key=api_key)
        model = "gpt-3.5-turbo"
        m = []
        for t in memory:
            m.append({"role": "user", "content": t[0]})
            m.append({"role": "assistant", "content": t[1]})
        messages = []
        messages.append(
            {
                "role": "system",
                "content": self.contruct_prompt()
            }
        )
        messages.extend(m)
        messages.append({"role": "user", "content": transcription})

        response = client.chat.completions.create(model=model, messages=messages)
        return response.choices[0].message.content
    
    def contruct_prompt(self): 
        prompt = f"you are helping to interview a candidate for the position of {self.interview.job_title}\
                as the interview progresses, please suggest the best questions possible, referencing their resume as needed : {self.interview.resume}\
                and how well they meet the requirements for the job description: {self.interview.job_description}"
        return prompt