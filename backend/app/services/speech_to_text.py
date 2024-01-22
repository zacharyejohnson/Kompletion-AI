
import speech_recognition as sr

class SpeechToTextService:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert_audio_to_text(self, audio_file_path):
        """
        Converts audio to text using Google Web Speech API.
        :param audio_file_path: Path to the audio file.
        :return: Extracted text as a string.
        """
        with sr.AudioFile(audio_file_path) as source:
            audio_data = self.recognizer.record(source)
            try:
                # Using Google Web Speech API for speech recognition
                text = self.recognizer.recognize_google(audio_data)
                return text
            except sr.UnknownValueError:
                # Error handling for unrecognized speech
                return "Speech was not understood"
            except sr.RequestError as e:
                # Error handling for API request issues
                return f"Could not request results from Google Speech Recognition service; {e}"

# Example usage
# speech_service = SpeechToTextService()
# text = speech_service.convert_audio_to_text('path/to/audio_file.wav')
# print(text)
