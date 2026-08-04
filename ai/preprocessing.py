"""
Preprocessing Module
--------------------
Expands slang, processes emojis,
and prepares text for sentiment analysis.
"""

import re
import emoji

from ai.slang import processor


def normalize_spaces(text: str) -> str:
    """
    Remove duplicate spaces.
    """

    return re.sub(r"\s+", " ", text).strip()


def convert_emojis(text: str) -> str:
    """
    😊 -> smiling face with smiling eyes
    """

    converted = emoji.demojize(
        text,
        delimiters=(" ", " ")
    )

    converted = converted.replace("_", " ")

    return normalize_spaces(converted)


def preprocess(text: str):

    original_text = text

    # Expand slang
    slang_result = processor.expand(text)

    expanded_text = slang_result["expanded_text"]

    # Convert emojis
    emoji_text = convert_emojis(expanded_text)

    # Normalize spaces
    final_text = normalize_spaces(emoji_text)

    return {

        "original_text": original_text,

        "processed_text": final_text,

        "slang_detected": slang_result["slang_detected"]

    }


if __name__ == "__main__":

    while True:

        text = input("\nEnter Text: ")

        if text.lower() == "exit":
            break

        result = preprocess(text)

        print("\nOriginal:\n")
        print(result["original_text"])

        print("\nProcessed:\n")
        print(result["processed_text"])

        print("\nDetected Slang:\n")

        if not result["slang_detected"]:
            print("None")

        else:

            for slang in result["slang_detected"]:

                print(
                    f"{slang['original']} -> {slang['replacement']}"
                )