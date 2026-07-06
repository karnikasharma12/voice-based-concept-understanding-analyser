"""
transcriber.py

Speech-to-Text Module using OpenAI Whisper

Author: Manish Sharma
Description:
    Converts audio files (.mp3, .wav, .m4a, .flac) into text.

Requirements:
    pip install openai-whisper torch ffmpeg-python
"""

import os
import logging
import whisper


class SpeechToText:
    """
    Speech-to-Text using OpenAI Whisper
    """

    SUPPORTED_FORMATS = (".mp3", ".wav", ".m4a", ".flac", ".ogg")

    def __init__(self, model_name: str = "base"):
        """
        Initialize Whisper model.

        Available models:
            tiny
            base
            small
            medium
            large
        """

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )

        logging.info("Loading Whisper model (%s)...", model_name)

        self.model = whisper.load_model(model_name)

        logging.info("Model loaded successfully.")

    def validate_audio(self, audio_path: str):
        """
        Validate audio file.
        """

        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"File not found: {audio_path}")

        extension = os.path.splitext(audio_path)[1].lower()

        if extension not in self.SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported format: {extension}\n"
                f"Supported: {self.SUPPORTED_FORMATS}"
            )

    def transcribe(self, audio_path: str) -> str:
        """
        Convert audio to text.

        Parameters
        ----------
        audio_path : str

        Returns
        -------
        transcript : str
        """

        self.validate_audio(audio_path)

        logging.info("Processing audio...")

        result = self.model.transcribe(
            audio_path,
            fp16=False
        )

        transcript = result["text"].strip()

        logging.info("Transcription completed.")

        return transcript

    def save_transcript(self, transcript: str, output_file="transcript.txt"):
        """
        Save transcript to file.
        """

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(transcript)

        logging.info("Transcript saved to %s", output_file)


if __name__ == "__main__":

    AUDIO_FILE = "sample.mp3"

    try:

        stt = SpeechToText(model_name="base")

        transcript = stt.transcribe(AUDIO_FILE)

        print("\n========== TRANSCRIPT ==========\n")
        print(transcript)

        stt.save_transcript(transcript)

    except Exception as e:
        logging.error(e)
