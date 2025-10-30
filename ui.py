from utils import yes_no, parse_int
from generator import generate_password_from_options
from strength_checker import check_password_strength

def show_menu():
    print("\n=== Password Tool CLI ===")
    print("[1] Generate password")
    print("[2] Check password strength")
    print("[3] Tips")
    print("[q] Quit")

def ask_generate_options() -> dict:
    length = parse_int("Password length (default 16): ", default=16, min_value=1)
    use_lower   = yes_no("Include lowercase?")
    use_upper   = yes_no("Include UPPERCASE?")
    use_digits  = yes_no("Include digits?")
    use_symbols = yes_no("Include symbols (!@#$%)?")
    enforce     = yes_no("Require at least one from each selected group?")
    return {
        "length": length,
        "use_lower": use_lower,
        "use_upper": use_upper,
        "use_digits": use_digits,
        "use_symbols": use_symbols,
        "enforce_rules": enforce,
    }

def print_generated_password(pwd: str):
    print(f"\nGenerated password: {pwd}")

def ask_password_to_check() -> str:
    return input("Enter password to check: ").strip()

def print_strength_report(report: dict):
    print(f"\nPassword strength: {report['rating']} ({report['score']}/4)")
    print("Reasons:")
    for r in report["reasons"]:
        print(f" - {r}")
    if report["suggestions"]:
        print("Suggestions:")
        for s in report["suggestions"]:
            print(f" • {s}")

def show_tips():
    print("""
How to build a strong password:
 - Use at least 12 characters (16+ better).
 - Mix lower/UPPER letters, digits, and symbols.
 - Avoid names, birthdays, and common words.
 - Don’t reuse passwords across accounts.
""".strip())

def run_app():
    while True:
        show_menu()
        option = input("> ").strip().lower()
        if option == "1":
            opts = ask_generate_options()
            try:
                pwd = generate_password_from_options(**opts)
                print_generated_password(pwd)
            except ValueError as e:
                print(f"Error: {e}")
        elif option == "2":
            pwd = ask_password_to_check()
            report = check_password_strength(pwd)
            print_strength_report(report)
        elif option == "3":
            show_tips()
        elif option in ("q", "quit", "exit"):
            print("Bye!")
            break
        else:
            print("Invalid option.")
