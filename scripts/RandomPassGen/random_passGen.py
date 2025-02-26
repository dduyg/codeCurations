import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """
    Generate a strong random password with customizable options.

    Parameters:
    - length (int): The desired length of the password (default is 12).
    - use_uppercase (bool): Whether to include uppercase letters (default is True).
    - use_digits (bool): Whether to include digits (default is True).
    - use_special_chars (bool): Whether to include special characters (default is True).

    Returns:
    - str: The generated password.
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Start with lowercase letters (always included)
    password_characters = lowercase

    # Add selected character sets based on the options
    if use_uppercase:
        password_characters += uppercase
    if use_digits:
        password_characters += digits
    if use_special_chars:
        password_characters += special_chars

    # Check that the password length is reasonable
    if length < 8:
        print("Warning: A strong password is usually 8 characters or more.")
    
    # Generate the password using random selection from the available characters
    password = ''.join(random.choice(password_characters) for _ in range(length))

    return password

def main():
    print("Password Generator")
    print("-------------------")

    # Get user inputs for the password options
    length = int(input("Enter password length (default is 12): ") or 12)
    use_uppercase = input("Include uppercase letters? (y/n, default is 'y'): ").lower() != 'n'
    use_digits = input("Include digits? (y/n, default is 'y'): ").lower() != 'n'
    use_special_chars = input("Include special characters? (y/n, default is 'y'): ").lower() != 'n'

    # Generate and display the password
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
