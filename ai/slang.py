"""
Gen Z Slang Processor
---------------------

Loads the slang dictionary and
expands Gen Z slang while
preserving metadata for the UI.
"""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SLANG_FILE = ROOT / "data" / "slang.json"


class SlangProcessor:

    def __init__(self):

        with open(SLANG_FILE, "r", encoding="utf-8") as file:
            self.dictionary = json.load(file)

    def expand(self, text: str):

        words = text.split()

        expanded = []

        detected = []

        for word in words:

            clean = word.lower().strip(".,!?;:\"'()[]{}")

            if clean in self.dictionary:

                info = self.dictionary[clean]

                expanded.append(info["replacement"])

                detected.append({

                    "original": word,

                    "replacement": info["replacement"],

                    "meaning": info["meaning"],

                    "category": info["category"]

                })

            else:

                expanded.append(word)

        return {

            "expanded_text": " ".join(expanded),

            "detected": detected

        }


processor = SlangProcessor()


if __name__ == "__main__":

    while True:

        text = input("\nText: ")

        if text.lower() == "exit":
            break

        result = processor.expand(text)

        print("\nExpanded:\n")

        print(result["expanded_text"])

        print("\nDetected:\n")

        if not result["detected"]:

            print("None")

        else:

            for item in result["detected"]:

                print(f"""
Original    : {item['original']}
Replacement : {item['replacement']}
Meaning     : {item['meaning']}
Category    : {item['category']}
""")