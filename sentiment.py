"""
Sentiment Analysis Module
-------------------------
Uses CardiffNLP Twitter RoBERTa
for sentiment analysis.
"""

import logging
import time

from transformers import pipeline

# Reduce Hugging Face logging
logging.getLogger("transformers").setLevel(logging.ERROR)

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

print(f"\nLoading {MODEL_NAME}...")

classifier = pipeline(
    task="sentiment-analysis",
    model=MODEL_NAME
)

print("✓ Sentiment model loaded.\n")


def analyze_sentiment(text: str) -> dict:
    """
    Analyze sentiment.

    Returns:
    {
        sentiment,
        confidence,
       processing_time_ms
    }
    """

    start = time.perf_counter()

    result = classifier(text)[0]

    elapsed = (time.perf_counter() - start) * 1000

    return {

        "sentiment": result["label"].capitalize(),

        "confidence": round(
            result["score"] * 100,
            2
        ),

        "processing_time_ms": round(
            elapsed,
            2
        )

    }


if __name__ == "__main__":

    while True:

        text = input("Enter text: ")

        if text.lower() == "exit":
            break

        output = analyze_sentiment(text)

        print("\nRESULT")
        print("----------------------------")
        print("Sentiment :", output["sentiment"])
        print("Confidence:", output["confidence"], "%")
        print("Time      :", output["processing_time_ms"], "ms")
        print()