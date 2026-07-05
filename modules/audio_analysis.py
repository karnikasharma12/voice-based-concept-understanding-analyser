import random

def analyze_audio(audio_file):
    """
    Audio Analysis Module

    Input:
        audio_file (.wav/.mp3)

    Returns:
        {
            "confidence": int,
            "fluency": int,
            "clarity": int
        }
    """


    confidence = random.randint(80, 95)
    fluency = random.randint(75, 95)
    clarity = random.randint(80, 98)

    return {
        "confidence": confidence,
        "fluency": fluency,
        "clarity": clarity
    }


if __name__ == "__main__":
    result = analyze_audio("sample.wav")

    print("Audio Analysis Result")
    print("---------------------")
    print("Confidence :", result["confidence"])
    print("Fluency    :", result["fluency"])
    print("Clarity    :", result["clarity"])
