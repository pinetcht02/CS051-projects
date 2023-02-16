"""
    CS051P Lab Assignments: Password Checking

    Name: Pine Netcharussaeng

    Date:   9/15/22

    The goal of this assignment is to familiarize you with the application
    of various different types of loops.
"""

# TODO: Implement code that helps the user choose a strong password. A strong
# password is defined as follows 
#      1. Password should contain at least 8 characters
#      2. Password should contain at least 2 lowercase letters
#      3. Password should contain at least 1 uppercase letter 
#      4. Password should contain at least 2 numbers 
#      5. Password should contain at least 1 character from !@#$


# Prompt user to input a password
password = input("Please enter a password:\n")

# Create condition for while loop to run when password is invalid
invalid_pass = True
while invalid_pass:

    # Establish counters for each criteria
    char_count = 0
    lower_count = 0
    upper_count = 0
    number_count = 0
    special_char = 0

# Count the letters in the password
    for letter in password:
        # For every letter in the password, count 1
        char_count = char_count + 1
        # For every lowercase letter, count 1
        if letter.islower():
            lower_count = lower_count + 1
        # For every uppercase letter, count 1
        if letter.isupper():
            upper_count = upper_count + 1
        # For every number in the password, count 1
        if letter.isnumeric():
            number_count = number_count + 1
        # For every special character, count 1
        if letter == "!" or letter == "@" or letter == "#" or letter == "$":
            special_char = special_char + 1

    # Create conditions for each criteria for the password
    # Prompt user if password has fewer than 8 characters
    if char_count < 8:
        print("Password should contain at least 8 characters.")
        password = input("Please enter your password:\n")
    # Prompt user if password has fewer than 2 lowercase letters
    elif lower_count < 2:
        print("Password should contain at least 2 lowercase letters.")
        password = input("Please enter your password:\n")
    # Prompt user if password has fewer than 1 uppercase letter
    elif upper_count < 1:
        print("Password should contain at least 1 uppercase letters.")
        password = input("Please enter your password:\n")
    # Prompt user if password has fewer than 2 numbers
    elif number_count < 2:
        print("Password should contain at least 2 numbers.")
        password = input("Please enter your password:\n")
    # Prompt user if password has fewer than 1 special character
    elif special_char < 1:
        print("Password should contain at least 1 character from !@#$")
        password = input("Please enter your password:\n")
    # If all above conditions satisfy, invalid_pass is now False; breaks while loop
    else:
        invalid_pass = False

print(password, "is a valid password!")
