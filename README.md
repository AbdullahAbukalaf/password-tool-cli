# 🔐 Password Tool CLI (Interactive CLI)

A simple and lightweight command-line tool built in Python to **generate secure passwords** and **check password strength** — all from your terminal.

It helps you create strong, random passwords, analyze their security, and get smart suggestions for improvement.

---

## 🚀 Features

* ✅ Generate random, secure passwords  
* ✅ Customize password length and character types  
* ✅ Enforce at least one of each selected character type  
* ✅ Check password strength (length, digits, symbols, variety)  
* ✅ Detect weak or common passwords instantly  
* ✅ Get improvement tips and best practices  
* ✅ Simple, menu-based CLI interface  
* ✅ No external libraries — built entirely with Python’s standard library

---

## 🌟 Preview

```text
=== Password Tool CLI ===
[1] Generate password
[2] Check password strength
[3] Tips
[q] Quit
> 1

Password length (default 16): 12
Include lowercase? [Y/N] y
Include UPPERCASE? [Y/N] y
Include digits? [Y/N] y
Include symbols (!@#$%)? [Y/N] y
Require at least one from each selected group? [Y/N] y

Generated password: %aT9L@d7s!Qf
```

### 🧠 Strength Check Example

```text
Checking password strength...
Enter password to check: MyPassword123!

Password strength: Strong (3/4)
Reasons:
 - Length is good (12).
 - Contains lowercase letters.
 - Contains uppercase letters.
 - Contains digits.
 - Contains symbols.
Suggestions:
 - Avoid common passwords.
```

---

## 🗂 Project Structure

```text
password-tool-cli/
├─ main.py               # Entry point (runs the CLI)
├─ ui.py                 # User interface (input/output)
├─ generator.py          # Password generation logic
├─ strength_checker.py   # Strength analysis logic
├─ utils.py              # Helper functions (validation, yes/no, parse_int)
├─ data/
│   ├─ __init__.py
│   └─ common_passwords.py   # Common password dataset (O(1) lookup)
├─ README.md             # Project documentation
└─ .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AbdullahAbukalaf/password-tool-cli.git
cd password-tool-cli
```

(Optional) create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux
```

Run the app:

```bash
python main.py
```

> 🧰 No dependencies needed — works with the built-in Python standard library.

---

## 🧱 Architecture Overview

| Layer        | File                  | Responsibility                                       |
| ------------- | --------------------- | ---------------------------------------------------- |
| Interface     | `ui.py`               | Prints menus, gets user input, displays results      |
| Logic         | `generator.py`        | Generates passwords securely using `secrets`         |
| Analysis      | `strength_checker.py` | Analyzes passwords and produces score/report         |
| Utilities     | `utils.py`            | Input helpers, validation, and reusable functions    |
| Data          | `common_passwords.py` | Stores common-password blacklist for O(1) lookups    |
| Entry Point   | `main.py`             | Launches the app and controls flow                   |

---

## 🔮 Future Plans

* [ ] Add password entropy calculation  
* [ ] Option to export generated passwords to a file  
* [ ] Include colorized CLI output  
* [ ] Add strength scoring visualization  
* [ ] Cloud sync with AWS S3 for password logs  

---

## 🧭 Version History

**v1.0.0 (current)**  
* Initial release  
* Password generator + strength checker + tips  

---

## 📜 License

MIT License © 2025 **Abdullah Abukalaf**

GitHub: [@AbdullahAbukalaf](https://github.com/AbdullahAbukalaf)

---


<p align="center">
  <b>Developed with ❤️ by <a href="https://github.com/AbdullahAbukalaf">Abdullah Abukalaf</a></b><br>
  <sub>Built for learning and real-world FastAPI practice.</sub>
</p>
