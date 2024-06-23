
---

# Password Complexity Checker and Strength Assessment

This Python script checks the complexity and assesses the strength of a given password based on specific criteria.

## Features

- **Password Complexity Check**: The `check_password_complexity` function verifies if a password meets the following criteria:
  - Length of at least 8 characters.
  - Contains at least one uppercase letter (`A-Z`).
  - Contains at least one lowercase letter (`a-z`).
  - Contains at least one digit (`0-9`).
  - Contains at least one special character or punctuation (`!@#$%^&*()-=_+[]{}|;':",./<>?`).

- **Password Strength Assessment**: The `assess_password_strength` function categorizes the strength of a password based on the number of criteria it meets:
  - **Very Weak**: Password length less than 8 characters.
  - **Weak**: Password meets only one criteria.
  - **Moderate**: Password meets two criteria.
  - **Strong**: Password meets three criteria.
  - **Very Strong**: Password meets all four criteria.
  - **Unknown**: If none of the criteria are met (though this should not happen if `check_password_complexity` passes).

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/password-checker.git
   cd password-checker
   ```

2. **Run the script:**

   Ensure you have Python installed. Then, execute the script:

   ```bash
   python password_checker.py
   ```

3. **Follow the prompts:**

   - Enter your password: [Your password here]

4. **Output:**

   - If the password meets the complexity criteria, it will display "Password meets complexity criteria" and indicate the strength (Very Weak, Weak, Moderate, Strong, or Very Strong).
   - If the password does not meet the complexity criteria, it will display "Password does not meet complexity criteria."

## Example

Checking and assessing the strength of a password:

```
Enter your password: MySecurePassword123!

Password meets complexity criteria.
Password strength: Very Strong
```

## Function Explanation

- `check_password_complexity(password)`: Checks if the password meets the specified complexity criteria and returns `True` or `False`.
- `assess_password_strength(password)`: Evaluates the strength of the password based on the number of criteria it satisfies and returns a corresponding strength level.

## Notes

- This script uses regular expressions (`re` module) to validate the password against complexity criteria.
- Adjust the criteria or add more rules as needed by modifying the regular expressions in the functions.

Feel free to use and modify this script to suit your own password validation needs!

---

# PRODIGY_CS_03
