"""
Smart Spell Correction
----------------------
Uses TextBlob while preserving
URLs, hashtags, mentions,
numbers and emojis.
"""

import re
from textblob import TextBlob


URL_PATTERN = r"https?://\S+|www\.\S+"
EMAIL_PATTERN = r"\S+@\S+\.\S+"
MENTION_PATTERN = r"@\w+"
HASHTAG_PATTERN = r"#\w+"
NUMBER_PATTERN = r"\d+"


PROTECTED = re.compile(
    f"{URL_PATTERN}|"
    f"{EMAIL_PATTERN}|"
    f"{MENTION_PATTERN}|"
    f"{HASHTAG_PATTERN}|"
    f"{NUMBER_PATTERN}"
)


def should_skip(word: str) -> bool:

    if PROTECTED.fullmatch(word):
        return True

    if len(word) <= 2:
        return True

    if not any(char.isalpha() for char in word):
        return True

    return False


def correct_text(text: str):

    words = text.split()

    corrected = []

    changes = []

    for word in words:

        if should_skip(word):

            corrected.append(word)
            continue

        new_word = str(TextBlob(word).correct())

        corrected.append(new_word)

        if new_word.lower() != word.lower():

            changes.append(
                {
                    "original": word,
                    "corrected": new_word
                }
            )

    return {

        "corrected_text": " ".join(corrected),

        "changes": changes

    }


if __name__ == "__main__":

    while True:

        text = input("\nEnter text: ")

        if text.lower() == "exit":
            break

        result = correct_text(text)

        print("\nCorrected:\n")

        print(result["corrected_text"])

        print("\nCorrections:\n")

        if not result["changes"]:

            print("None")

        else:

            for change in result["changes"]:

                print(
                    f"{change['original']} -> {change['corrected']}"
                )