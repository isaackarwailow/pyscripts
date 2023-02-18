import random
import string

def generate_password(length):
    # Define the character sets to use for the password
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    # Combine the character sets
    all_chars = letters + numbers + symbols

    # Generate a random password of the specified length
    password = ''.join(random.choice(all_chars) for i in range(length))

    return password

# Generate a 12-character password and print it to the console
password = generate_password(12)
print("Your password is:", password)