# SPDX-License-Identifier: MIT
import os

JOKE = "I let my AI coding agent run the demo since it wrote all the code — it crashed on the first click and asked if I wanted it to generate a working version."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
