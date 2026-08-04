"""
Loads Gen Z slang dictionary
and expands slang before
sentiment analysis.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLANG_FILE = ROOT / "data" / "slang.json"


class SlangProcessor:

    def __init__(self):

        with open(SLANG_FILE, "r", encoding="utf-8") as file:

            self.slang = json.load(file)

    def expand(self, text: str):

        words = text.split()

        expanded_words = []

        detected = []

        for word in words:

            clean = word.lower().strip(".,!?;:\"'()[]{}")

            if clean in self.slang:

                replacement = self.slang[clean]["replacement"]

                expanded_words.append(replacement)

                detected.append({
                    "original": word,
                    "replacement": replacement
                })

            else:

                expanded_words.append(word)

        return {

            "expanded_text": " ".join(expanded_words),

            "slang_detected": detected

        }


processor = SlangProcessor()


if __name__ == "__main__":

    while True:

        text = input("\nEnter Text: ")

        if text.lower() == "exit":
            break

        result = processor.expand(text)

        print("\nExpanded Text:\n")

        print(result["expanded_text"])

        print("\nDetected Slang:\n")

        for item in result["slang_detected"]:

            print(
                f"{item['original']}  →  {item['replacement']}"
            )

        print()