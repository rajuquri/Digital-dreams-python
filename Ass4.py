def check_password_strength(password):
    if len(password) < 8:
        return "Weak Password: Must be at least 8 characters long"

    has_digit = False
    has_special = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
        elif not ch.isalnum():
            has_special = True

    if not has_digit:
        return "Weak Password: Must contain at least one digit"

    if not has_special:
        return "Weak Password: Must contain at least one special character"

    return "Strong Password"
print(check_password_strength("Pass@123"))  