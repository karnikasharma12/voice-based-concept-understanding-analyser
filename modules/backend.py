import os
import tempfile

from modules.speech_to_text import SpeechToText
from modules.semantic_analysis import analyze as semantic_analyze
from modules.audio_analysis import analyze_audio
from modules.AI_summary import generate_summary


REFERENCE_TEXT = """
Artificial Intelligence is the simulation of human intelligence by machines.
Machine learning is a branch of AI that enables computers to learn from data.
"""


def analyze(audio):

    if audio is None:
        return {
            "transcript": "",
            "score": 0,
            "confidence": 0,
            "fluency": 0,
            "clarity": 0,
            "summary": "No audio uploaded."
        }

    # Save uploaded file with original extension
    extension = os.path.splitext(audio.name)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=extension) as temp:
        temp.write(audio.getbuffer())
        temp_path = temp.name

    try:
        # Speech to Text
        stt = SpeechToText(model_name="tiny")
        transcript = stt.transcribe(temp_path)

        # Semantic Analysis
        score = semantic_analyze(REFERENCE_TEXT, transcript)

        # Keep score between 0 and 100
        score = max(0, min(100, score))

        # Audio Analysis
        audio_result = analyze_audio(temp_path)

        # AI Summary
        summary = generate_summary(transcript)

        return {
            "transcript": transcript,
            "score": score,
            "confidence": audio_result["confidence"],
            "fluency": audio_result["fluency"],
            "clarity": audio_result["clarity"],
            "summary": summary
        }

    except Exception as e:
        return {
            "transcript": "",
            "score": 0,
            "confidence": 0,
            "fluency": 0,
            "clarity": 0,
            "summary": f"Error: {str(e)}"
        }

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)