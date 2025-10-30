import string, secrets

def generate_password_from_options(
    length: int,
    use_lower: bool,
    use_upper: bool,
    use_digits: bool,
    use_symbols: bool,
    enforce_rules: bool,
) -> str:
    groups = []
    if use_lower:   groups.append(string.ascii_lowercase)
    if use_upper:   groups.append(string.ascii_uppercase)
    if use_digits:  groups.append(string.digits)
    if use_symbols: groups.append(string.punctuation)

    if not groups:
        raise ValueError("No character groups selected.")
    if enforce_rules and length < len(groups):
        raise ValueError(f"Length {length} too short for {len(groups)} required groups.")

    pool = "".join(groups)

    chars = []
    if enforce_rules:
        for g in groups:
            chars.append(secrets.choice(g))

    while len(chars) < length:
        chars.append(secrets.choice(pool))

    for i in range(len(chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        chars[i], chars[j] = chars[j], chars[i]

    return "".join(chars)
