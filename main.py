import logging
import time
from backend.app.models.interview_model import Interview
from backend.app.services.speech_to_text import SpeechToTextService
from ai.models.LLM_reponder import OpenAIResponder
import gradio as gr

# Configuration (could be moved to a separate config file or environment variables)
RESUME_PATH = "backend\\data\\resumes\\Zach Johnson Resume 2023.pdf"
JOB_DESCRIPTION_PATH = "backend\\data\\job_descriptions\\ai-ml-risk.txt"
COMPANY_DATA_PATH = "backend\\data\\company_data\\fanniemae.txt"

# Initialize logging
logging.basicConfig(level=logging.INFO)

def initialize_interview():
    """Initializes the interview object with provided data."""
    try:
        return Interview("Assessment of AI/ML Risks - Advisor", "Zach", "Zach", JOB_DESCRIPTION_PATH, RESUME_PATH, company=COMPANY_DATA_PATH)
    except Exception as e:
        logging.error(f"Error initializing the interview: {e}")
        return None

def toggle_listening(listening):
    """Toggles the listening state."""
    return not listening if listening else listening

def process_audio(audio_data, listening, last_question_time, ai, stt):
    """Processes the audio data to transcribe and generate questions."""
    current_time = time.time()
    if listening:
        transcription = stt.transcribe(audio_data)
        if last_question_time is None or current_time - last_question_time >= 10:
            question = ai.construct_prompt(transcription)
            last_question_time = current_time
            return transcription, question, last_question_time
        return transcription, "", last_question_time
    return "", "", last_question_time

def main():
    interview = initialize_interview()
    if interview is None:
        return

    ai = OpenAIResponder(interview=interview)
    stt = SpeechToTextService(ai)

    listening = False
    last_question_time = None

    with gr.Blocks() as demo:
        with gr.Row():
            start_stop_button = gr.Button("Start Listening")
            transcription_area = gr.Textbox()
            question_area = gr.Textbox()

        # Assuming you have a text component to update, replace "text_component" with the actual component
        # If there's no component to update, you can just use [start_stop_button]
        start_stop_button.click(fn=lambda: toggle_listening(listening), outputs=[start_stop_button])

        audio = gr.Audio(streaming=True)

        audio.stream(fn=lambda data: process_audio(data, listening, last_question_time, ai, stt), inputs=audio, outputs=[transcription_area, question_area])
        
    demo.launch()



if __name__ == "__main__":
    main()
