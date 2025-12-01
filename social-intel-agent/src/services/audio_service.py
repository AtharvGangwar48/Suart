import speech_recognition as sr
from pydub import AudioSegment

class AudioService:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def extract_audio_from_video(self, video_path: str) -> str:
        audio = AudioSegment.from_file(video_path)
        audio_path = video_path.replace('.mp4', '.wav')
        audio.export(audio_path, format="wav")
        return audio_path
    
    def speech_to_text(self, audio_path: str) -> str:
        try:
            with sr.AudioFile(audio_path) as source:
                audio = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio)
                return text
        except Exception:
            return ""