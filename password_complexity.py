import re

def check_password_complexity(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    if (length_criteria and uppercase_criteria and lowercase_criteria
        and digit_criteria and special_char_criteria):
        return True
    else:
        return False

def assess_password_strength(password):
    length = len(password)
    complexity_score = 0

    if length < 8:
        return "Very Weak"

    if re.search(r'[A-Z]', password):
        complexity_score += 1
    if re.search(r'[a-z]', password):
        complexity_score += 1
    if re.search(r'\d', password):
        complexity_score += 1
    if re.search(r'[\W_]', password):
        complexity_score += 1

    if complexity_score == 1:
        return "Weak"
    elif complexity_score == 2:
        return "Moderate"
    elif complexity_score == 3:
        return "Strong"
    elif complexity_score == 4:
        return "Very Strong"
    else:
        return "Unknown"

if __name__ == "__main__":
    password = input("Enter your password: ")

    if check_password_complexity(password):
        print("Password meets complexity criteria.")
        strength = assess_password_strength(password)
        print(f"Password strength: {strength}")
    else:
        print("Password does not meet complexity criteria.")
