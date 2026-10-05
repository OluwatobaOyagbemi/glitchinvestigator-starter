# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Purpose:** A Streamlit number-guessing game. You pick a difficulty, guess the secret number within a limited number of attempts, and get higher/lower hints and a score.

**Bugs found:**
- Hints were reversed ("Go HIGHER" when the guess was too high).
- On even attempts the secret was cast to a string, so comparisons were string-based (`"9" > "10"`).
- Hard (1-50) was easier than Normal (1-100).
- Attempts started at 1, so the game ended a guess early, and invalid input cost an attempt.
- New Game ignored the difficulty range and didn't reset score, status or history; changing difficulty kept the old secret.
- The info text hardcoded "1 and 100".
- Win points were off by one, and a wrong "Too High" guess scored +5 on even attempts.
- Floats such as `7.9` were silently truncated and out-of-range guesses were accepted.

**Fixes applied:** The core logic moved into `logic_utils.py` and was fixed there (hints, numeric comparison, ranges, parsing, scoring). `app.py` now keeps the secret as an int, counts only valid guesses, and resets all state through one `start_new_game()` helper. Each fix has a pytest case in `tests/test_game_logic.py`.

## 📸 Demo Walkthrough

1. Run `python -m streamlit run app.py` and pick a difficulty in the sidebar; the range and attempt limit shown match that difficulty.
2. Type a non-number, a decimal, or a number outside the range: an error appears and the attempts counter does not change.
3. Guess a valid number: the hint now points the right way ("Go LOWER!" for a guess above the secret) and the score drops by 5.
4. Keep guessing until you win (balloons, final score) or run out of attempts (game over, secret revealed).
5. Click **New Game** or change difficulty: the secret, attempts, score, status and history all reset.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0 -- /Users/USER/glitchinvestigator-starter/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/USER/glitchinvestigator-starter
collecting ... collected 8 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 12%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 25%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 37%]
tests/test_game_logic.py::test_comparison_is_numeric_not_string PASSED   [ 50%]
tests/test_game_logic.py::test_hard_range_is_larger_than_normal PASSED   [ 62%]
tests/test_game_logic.py::test_parse_guess_rejects_non_numbers_and_floats PASSED [ 75%]
tests/test_game_logic.py::test_parse_guess_enforces_range PASSED         [ 87%]
tests/test_game_logic.py::test_score_first_guess_win_and_wrong_guesses PASSED [100%]

============================== 8 passed in 0.02s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
