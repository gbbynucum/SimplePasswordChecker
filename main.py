# Define a function to check if a password meets the complexity requirements based on the chosen difficulty level
def check_password(password, difficulty):
    # Check requirements based on the chosen difficulty level
    if difficulty == "Easy":
        # Check if the password has at least 6 characters
        if len(password) >= 6:
            return True
        else:
            return "Password must be at least 6 characters long"
    elif difficulty == "Medium":
        # Check if the password has at least 8 characters, contains at least one uppercase letter, one lowercase letter, and one digit
        if len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password):
            return True
        else:
            feedback = []
            # Provide specific feedback on what's missing in the password
            if len(password) < 8:
                feedback.append("Password must be at least 8 characters long")
            if not any(c.isupper() for c in password):
                feedback.append("Password must contain at least one uppercase letter")
            if not any(c.islower() for c in password):
                feedback.append("Password must contain at least one lowercase letter")
            if not any(c.isdigit() for c in password):
                feedback.append("Password must contain at least one digit")
            return ", ".join(feedback)
    elif difficulty == "Hard":
        # Check if the password meets the requirements for Hard level (all requirements for Medium level plus at least one special character)
        if len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(not c.isalnum() for c in password):
            return True
        else:
            feedback = []
            # Provide specific feedback on what's missing in the password
            if len(password) < 8:
                feedback.append("Password must be at least 8 characters long")
            if not any(c.isupper() for c in password):
                feedback.append("Password must contain at least one uppercase letter")
            if not any(c.islower() for c in password):
                feedback.append("Password must contain at least one lowercase letter")
            if not any(c.isdigit() for c in password):
                feedback.append("Password must contain at least one digit")
            if not any(not c.isalnum() for c in password):
                feedback.append("Password must contain at least one special character")
            return ", ".join(feedback)
    else:
        return "Invalid difficulty level"

# Define the main function to allow the user to select a difficulty level and enter a password
def main():
    # Repeat the process until the user provides a valid difficulty level
    while True:
        difficulty = input("Choose difficulty level (Easy, Medium, Hard): ").capitalize()
        if difficulty not in ["Easy", "Medium", "Hard"]:
            print("Invalid difficulty level. Please choose again.")
            continue
        else:
            print(f"Chosen difficulty level: {difficulty}")
            print("Requirements:")
            # Display the requirements for the chosen difficulty level
            if difficulty == "Easy":
                print("- At least 6 characters")
            elif difficulty == "Medium":
                print("- At least 8 characters\n- At least one uppercase letter\n- At least one lowercase letter\n- At least one digit")
            elif difficulty == "Hard":
                print("- At least 8 characters\n- At least one uppercase letter\n- At least one lowercase letter\n- At least one digit\n- At least one special character")
            # Prompt the user to enter a password
            password = input("Enter your password: ")
            # Check if the password meets the requirements for the chosen difficulty level and provide feedback
            result = check_password(password, difficulty)
            if result is True:
                print("Password meets the requirements. Good to go!")
            else:
                print("Password does not meet the requirements. Please try again.")
                print("Reasons:", result)

# Execute the main function
if __name__ == "__main__":
    main()
