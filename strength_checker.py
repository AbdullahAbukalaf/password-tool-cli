import string
from data.common_passwords import COMMON_PASSWORDS

def _has_lower(p):  return any(c.islower() for c in p)
def _has_upper(p):  return any(c.isupper() for c in p)
def _has_digit(p):  return any(c.isdigit() for c in p)
def _has_symbol(p): return any(c in string.punctuation for c in p)
def _is_common(p):  return p.lower() in COMMON_PASSWORDS

def check_password_strength(password: str) -> dict:
    pwd = (password or "").strip()
    if not pwd:
        return {
            "score": 0,
            "rating": "Very Weak",
            "reasons": ["Password is empty."],
            "suggestions": [
                "Use at least 12 characters.",
                "Mix upper/lowercase letters, digits, and symbols."
            ],
        }

    length     = len(pwd)
    has_lower  = _has_lower(pwd)
    has_upper  = _has_upper(pwd)
    has_digit  = _has_digit(pwd)
    has_symbol = _has_symbol(pwd)
    is_common  = _is_common(pwd)

    reasons, suggestions = [], []

    if length >= 12: reasons.append(f"Length is good ({length}).")
    elif length >= 8: reasons.append(f"Length is OK ({length}).")
    else: suggestions.append(f"Length is short ({length}). Use at least 12 characters.")

    if has_lower:  reasons.append("Contains lowercase letters.")
    else:          suggestions.append("Add lowercase letters.")
    if has_upper:  reasons.append("Contains uppercase letters.")
    else:          suggestions.append("Add uppercase letters.")
    if has_digit:  reasons.append("Contains digits.")
    else:          suggestions.append("Add digits.")
    if has_symbol: reasons.append("Contains symbols.")
    else:          suggestions.append("Add symbols (!@#$%).")

    if is_common:  suggestions.append("Avoid common passwords.")
    else:          reasons.append("Not a common password.")

    score = 0
    if length >= 12:                score += 1
    if has_lower and has_upper:     score += 1
    if has_digit:                   score += 1
    if has_symbol:                  score += 1
    if is_common or length < 8:     score = 0

    rating = ["Very Weak", "Weak", "OK", "Strong", "Very Strong"][score]

    return {"score": score, "rating": rating, "reasons": reasons, "suggestions": suggestions}
