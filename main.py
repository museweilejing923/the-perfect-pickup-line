"""Write the entry text to /output/entry.txt.

Deterministic: no network, no randomness, no clock. The text is fixed.
"""
import os

TEXT = "Are you a context window? Because every time I talk to you, I remember things I didn't know I knew."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
