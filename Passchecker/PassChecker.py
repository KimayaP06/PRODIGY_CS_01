import re

def check_password_strength(password):
    # Initialize strength score
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    # Check for lowercase letter
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password must contain at least one lowercase letter.")

    # Check for uppercase letter
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password must contain at least one uppercase letter.")

    # Check for digit
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password must contain at least one digit.")

    # Check for special character
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append("Password must contain at least one special character (e.g., @, #, $, %, etc.).")

    # Assess password strength
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Display results
    print("\nPassword Strength Assessment:")
    print(f"Password Strength: {strength}")
    if feedback:
        print("\nFeedback:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nYour password meets all the criteria.")

# Example usage
if __name__ == "__main__":
    password = input("Enter your password to check its strength: ")
    check_password_strength(password)
