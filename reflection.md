# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

I used Claude Code in VS Code for this project. It marked suspected bugs in `app.py` with FIXME comments, moved the core logic into `logic_utils.py`, and fixed bugs one at a time.

**Correct suggestion:** Claude suggested that the hot spot for the "random" behavior was the submit handler converting the secret to `str` on even attempts, which made `check_guess` compare strings (so `"9" > "10"`). It was correct because the same guess gave different hints depending on whether the attempt number was odd or even. The fix was to pass `st.session_state.secret` as an int and drop the `try/except TypeError` fallback that only existed to hide the problem. I verified it with a pytest case, `check_guess(9, 10)`, which must return "Too Low" (it would be "Too High" as strings).

**Suggestion I did not accept as written:** The starter test file expected `check_guess` to return only an outcome string like `"Win"`, while the game code and the `logic_utils.py` docstring use an `(outcome, message)` tuple. Rather than rewrite `check_guess` to match the old tests (which would break the hint messages in the UI), I kept the tuple and changed the tests to unpack it. I also made the hint tests assert the message text, since the reversed-hints bug lived in the message. I verified by running pytest and confirming all the tests pass.

---

## 3. Debugging and testing your fixes

- **How I decided a bug was fixed:** a bug counted as fixed only when a pytest case that targeted it failed before the change and passed after, and the other tests still passed. For the hint bug the test is a guess of 60 against a secret of 50, which must return "Too High" with a "LOWER" message.
- **Tests I ran:** `python -m pytest` runs four tests in `tests/test_game_logic.py`: winning guess, too high, too low, and numeric-not-string comparison. The last one showed that the odd/even behavior was a type problem, not a logic problem in the comparison itself.
- **How AI helped with tests:** Claude suggested the tests, and the string-comparison edge case (`9` vs `10`) came from its explanation of why string comparison breaks. I also ran the app with `streamlit run app.py` and played it: invalid input, hint direction, difficulty changes and New Game all behaved correctly.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
