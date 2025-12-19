## `random_passGen.py`
_Generate strong, random passwords with customizable options using this Python script. It allows you to specify the length and complexity of the password, including options for uppercase letters, digits, and special characters:_
- **Customizable Length**: Choose the desired length of the password (default is 12 characters).
- **Character inclusion**: Uppercase, digits, and special characters (like `!`, `@`, `#`, etc.) can be toggled *on* or *off*.
- **Randomization**: Passwords are generated with secure randomness.

## How to Use
1. Run the script with the following command:
```bash
python random_passGen.py
```
2. The script will prompt you to:
    - Enter the desired password length (default is 12).
    - Choose whether to include uppercase letters, digits, and special characters by responding with 'y' (yes) or 'n' (no).
3. After entering the options, the script will display a randomly generated password based on the provided criteria.

### Example Output:
```
Password Generator
-------------------
Enter password length (default is 12): 16
Include uppercase letters? (y/n, default is 'y'): y
Include digits? (y/n, default is 'y'): y
Include special characters? (y/n, default is 'y'): y

Generated Password: sJ3!kL8@M1wzG7hB
```

### Default Settings:
- **Length**: 12 characters
- **Uppercase Letters**: Included by default
- **Digits**: Included by default
- **Special Characters**: Included by default

You can modify these options to suit your needs.

## Code Explanation
1. **Imports**:
    - `random`: For selecting characters randomly.
    - `string`: Defines different sets of characters like lowercase letters, uppercase letters, digits, and special characters.
2. **Password Generation Logic**:
    - The `generate_password` function combines selected character sets and generates a password of the specified length.
    - The password is randomly generated using Python’s `random.choice()` function.
3. **User Input**:
    - The script asks for user input to customize the password generation, such as password length and character inclusion options.
4. **Password Output**:
    - The generated password is printed in the console.

## Security Note
Always ensure that the password generated is long enough (8 characters or more is recommended).

It prints a warning if the length is set to below 8 characters (suggesting stronger passwords be at least 8 characters long). Strong passwords are crucial for security.
