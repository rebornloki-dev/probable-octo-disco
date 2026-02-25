# Changelog

All notable changes to this project will be documented in this file.

Note that all changes before 2026-02-20 were not documented.

## [1.2.1] - 2026-02-24
### Added
- Created `fakest-bank-youve-seen.py` with dictionary-based account storage.
- Implemented `login.py` for separate authentication testing.

### Fixed
- **The "Jerry" Bug:** Fixed `NameError` where `amount` was called before being defined.
- **Type Mismatch:** Corrected PIN comparison logic from Integer to String to handle leading zeros.

### Changed
- Reorganized file structure for better readability and "browsability."
- Updated README to reflect the 3-year roadmap to Assembly.

---

## [1.2.0] - 2026-02-20
### Added
- Initial banking logic using simple variables.
- Basic `if/else` structures for balance checking.