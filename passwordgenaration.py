import random
import string

# Use built-in constants for characters
chars = string.ascii_letters + string.digits + string.punctuation

# Generate a password of length 8
password = ''.join(random.choice(chars) for _ in range(8))

print("Generated password:", password)
