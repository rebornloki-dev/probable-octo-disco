# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project follows [Semantic Versioning](https://semver.org/).
- Plsss help my copilot quota was reached
## [1.2.1.5] - 2026-04-07

### Added

- Added conditional logic to `Loops & Iterations/intro.py` to print 'found!' when number 3 is encountered in the loop.
- Added educational comments to `Loops & Iterations/while-loops.py` to explain while loops, infinite loops, and the `break` statement.

### Changed

- Added comprehensive learning-focused comments to all Python scripts for educational reference:
  - `Practices/1a.py` — temperature conditional logic
  - `Practices/fakest-bank-youve-seen.py` — ATM bank system with dictionaries
  - `Practices/practice.py` — variables and user input/output
  - `Practices/test.py` — references vs. copies and mutability
  - `Conditionals/log_in_screen.py` — OR operator logic
  - `Conditionals/Basic_conditionals.py` — string comparison and if/elif/else
  - `Booleans/a_suspiscious_list.py` — object identity with `is` operator
  - `Booleans/log_in_screen.py` — NOT operator
  - `Sets & Tuples/tuples.py` — tuple immutability
  - `Dumb Stuff/finalfinal.py` — simple guessing game
  - `Dumb Stuff/haha.py` — string input and conditionals
  - `Dumb Stuff/frame_counter.py` — video analysis with OpenCV
  - `Loops & Iterations/loop.py` — nested loops

---

## [1.2.1.4] - 2026-03-02

### Added

- Initial implementation of number printing logic in `Loops & Iterations/intro.py`.

---

## [1.2.1.3] - 2026-03-01

### Added

- New `Booleans/` directory with boolean learning scripts:
  - `Booleans/a_suspiscious_list.py` — demonstrates object identity with `is` operator.
  - `Booleans/false_values.py` — documents Python's falsy values (False, None, 0, empty sequences/mappings).
  - `Booleans/log_in_screen.py` — simple login example using `not` operator.

### Changed

- Updated `Conditionals/log_in_screen.py` to use `or` for checking if user is `'Admin'` OR logged in.

---

## [1.2.1.2] - 2026-02-24

### Added

- New practice scripts and demos:
  - `Conditionals/Basic_conditionals.py` — basic conditional example.
  - `Dictionaries/dictionaries.py` — dictionary examples and `student` demo.
  - `Sets & Tuples/learning_sets.py` — set operations (union, intersection, difference).
  - `Sets & Tuples/tuples.py` — tuple immutability demo (needs fix).
  - `Practices/practice.py`, `Practices/test.py` — simple I/O and mutability demos.
  - `Practices/fakest-bank-youve-seen.py` — basic banking simulation using an `account` dictionary.
  - `Dumb Stuff/frame_counter.py` — `analyze_video` utility using OpenCV.
  - `Dumb Stuff/finalfinal.py`, `Dumb Stuff/haha.py` — small games/inputs.
  - Added auxiliary test and practice scripts.

### Changed

- README updated to describe goals, structure, and run instructions.
- Repository reorganized into folders for clarity (Conditionals, Dictionaries, Sets & Tuples, Practices, Dumb Stuff).
- README and CHANGELOG added/updated.
- Reorganized files for improved discoverability.

### Fixed

- Banking example: fixed withdrawal logic and PIN handling (PIN treated as string; `amount` defined before use).
- Resolved `NameError` in banking example where `amount` was referenced before assignment.
- Corrected PIN comparison to treat PINs as strings to preserve leading zeros.
- Minor script corrections and clarity improvements across examples.

---

## [1.2.0] - 2026-02-20

### Added

- Initial banking logic and basic balance check examples.

---

## [1.0.0] - 2026-02-15

### Added

- Initial repository bootstrap with Python practice scripts demonstrating dictionaries, sets, tuples, conditionals, and small utilities.
- Added README and LICENSE (MIT).

---

## Notes

- TODO: fix tuple immutability example in [`Sets & Tuples/tuples.py`](Sets%20%26%20Tuples/tuples.py).
- Consider making `Dumb Stuff/frame_counter.py` accept a command-line argument for `video_path` instead of an in-file constant.
