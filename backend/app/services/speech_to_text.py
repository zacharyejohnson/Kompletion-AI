
import soundcard as sc
import soundfile as sf
import threading
import os
import queue
import speech_recognition as sr
import time
from transformers import pipeline
import numpy as np
import torch
from ai.models.LLM_reponder import OpenAIResponder
import gradio as gr

class SpeechToTextService:
    def __init__(self, ai):

        self.ai = ai
        
        gpu_available = torch.cuda.is_available()  # Nvidia GPU
        mps_available = (
                hasattr(torch.backends, "mps") and torch.backends.mps.is_available()
            )  # Apple Metal (M1/M2/M3)
        xpu_available = hasattr(torch, "xpu") and torch.xpu.is_available()  # Intel XPU

        self.transcriber = pipeline(
                "automatic-speech-recognition",
                model="openai/whisper-base.en",
                device="cuda"
                if gpu_available
                else "xpu"
                if xpu_available
                else "mps"
                if mps_available
                else "cpu",
            )



    def transcribe(self, cookie, new_chunk, job_title):
        sr, y = new_chunk
        y = y.astype(np.float32)
        if isinstance(
            y[0], np.ndarray
        ):  # If we get a stereo signal, let's average those waves
            y = np.mean(y, axis=1)
        abs_y = np.abs(y)
        avg_y = np.mean(np.abs(y))
        if avg_y < 100:
            
                answer = self.ai.process_oai(
                        cookie["transcription"], cookie["memory"], job_title
                    )
               
                cookie["answer"] += "🤖 " + answer + "\n"

                cookie["memory"].append((cookie["transcription"], answer))
                cookie["memory"] = cookie["memory"][-20:]

                cookie["hear"] += "🎙️ " + cookie["transcription"] + "\n"
                cookie["transcription"] = ""
                cookie["stream"] = None
        else:
            y /= np.max(abs_y)
            if cookie["stream"] is not None:
                cookie["stream"] = np.concatenate([cookie["stream"], y])
            else:
                cookie["stream"] = y

            cookie["transcription"] = self.transcriber(
                {"sampling_rate": sr, "raw": cookie["stream"]}
            )["text"]

        return cookie, cookie["hear"] + cookie["transcription"], cookie["answer"]

