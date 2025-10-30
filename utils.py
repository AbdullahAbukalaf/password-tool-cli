def yes_no(prompt: str) -> bool:
    while True:
        ans = input(f"{prompt} [Y/N] ").strip().lower()
        if ans in ("y", "yes"): return True
        if ans in ("n", "no"):  return False
        print("Please enter Y or N.")

def parse_int(prompt: str, default: int, min_value: int | None = None, max_value: int | None = None) -> int:
    raw = input(prompt).strip()
    if raw == "":
        return default
    try:
        val = int(raw)
    except ValueError:
        print(f"Invalid number. Using default {default}.")
        return default
    if min_value is not None and val < min_value:
        print(f"Must be ≥ {min_value}. Using {min_value}.")
        return min_value
    if max_value is not None and val > max_value:
        print(f"Must be ≤ {max_value}. Using {max_value}.")
        return max_value
    return val
