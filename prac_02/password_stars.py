"""
Write a program that asks the user for a password,
with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
"""

PASSWORD_MIN_LENGTH = 10


def main():
    """Program to take a password and convert into asterisks"""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print length asterisks"""
    print('*' * len(password))


def get_password():
    """Determine if password meets minimum character length"""
    password = input("Enter password: ")
    while len(password) < PASSWORD_MIN_LENGTH:
        print(f"Password must be {PASSWORD_MIN_LENGTH} characters")
        password = input("Enter password: ")
    return password


main()
