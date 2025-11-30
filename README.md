Guess-the-Word

A simple, fun word-guessing game built with Python. Great for quick breaks and practicing pattern recognition.

Overview

Guess the secret word one letter at a time. You have a limited number of attempts; wrong guesses reduce your chances, and correct guesses reveal letters. Win by uncovering the full word before you run out of attempts.

Features

- Classic gameplay: Letter-by-letter guessing with win/lose conditions.
- Word list: Play with a predefined set or your own custom words.
- Progress display: See revealed letters and remaining attempts.
- Input validation: Handles repeated and invalid guesses cleanly.

Requirements

- Python: 3.8 or newer
- OS: Windows, macOS, or Linux
- Optional: A terminal/command prompt if running via CLI

Installation

Quick run (Windows):
- Download: Save the game folder or .py file to your Desktop.
- Double-click: If associated with Python, double-click the file to start.

Command line (all platforms):
1. Download: Save guess_the_word.py locally.
2. Open terminal: Command Prompt (Windows) or Terminal (macOS/Linux).
3. Navigate:
   cd path/to/your/download
4. Run:
   python guess_the_word.py
   or, if your system uses python3:
   python3 guess_the_word.py

How to play

- Goal: Guess the hidden word before attempts run out.
- Input: Type a single letter and press Enter.
- Feedback:
  - Correct guess: Letter appears in the word.
  - Incorrect guess: Attempts decrease.
  - Repeat guess: You’ll be notified; attempts won’t change.
- Win/Lose:
  - Win: All letters revealed.
  - Lose: Attempts reach zero; the word is shown.

Example session

Guess the Word!
_ _ _ _ _
Attempts left: 6
Enter a letter: e
Good guess!
_ e _ _ _
Attempts left: 6
Enter a letter: x
Nope!
_ e _ _ _
Attempts left: 5
...

Customization

- Change attempts: Edit MAX_ATTEMPTS in the code to increase/decrease difficulty.
- Use your words: Replace or extend WORD_LIST = ["apple", "robot", ...] with your own set.
- Reveal style: Adjust how underscores or spacing are printed for readability.

Troubleshooting

- Double-click doesn’t start: Ensure Python is installed and .py files are associated with Python.
- Command not found (python): Try python3, or add Python to your system PATH.
- Non-English keyboard input issues: Stick to A–Z letters; sanitize input in code if needed.

