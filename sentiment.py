from transformers import pipeline
import logging
import time


# Reduce Hugging Face console spam
logging.getLogger("transformers").setLevel(logging.ERROR)


print("Loading sentiment model...")

# Load model only once
sentiment_model = pipeline(
    task="sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

print("Sentiment model loaded!")


def analyze_sentiment(text: str):
    """
    Takes text and returns sentiment prediction.

    Output:
    {
        "sentiment": "positive",
        "confidence": 98.52,
        "time_ms": 45.2
    }
    """

    start = time.perf_counter()

    result = sentiment_model(text)[0]

    end = time.perf_counter()

    label = result["label"].lower()

    confidence = round(
        result["score"] * 100,
        2
    )

    return {
        "sentiment": label,
        "confidence": confidence,
        "time_ms": round((end - start) * 1000, 2)
    }


# Testing
if __name__ == "__main__":

    while True:

        text = input("\nEnter text: ")

        if text.lower() == "exit":
            break

        output = analyze_sentiment(text)

        print("\nResult")
        print("----------------")
        print("Sentiment :", output["sentiment"])
        print("Confidence:", output["confidence"], "%")
        print("Time      :", output["time_ms"], "ms")