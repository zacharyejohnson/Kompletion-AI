import speech_recognition as sr
from .backend.app.services.question_generator import QuestionGenerator
def main(): 
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    qg = QuestionGenerator(api_key="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")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening to the interview...")

        while True:
            try:
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                transcript = recognizer.recognize_google(audio)
                print(f"Candidate said: {transcript}")
                question = generate_question(context, transcript)
                print(f"Suggested question: {question}")
            except sr.WaitTimeoutError:
                print("No speech detected. Continuing to listen...")
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError:
                print("Error with the speech recognition service")


if __name__ == "__main__": 
    main()
