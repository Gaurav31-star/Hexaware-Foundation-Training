import string
import random

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(12))
    return password

generated_password = generate_password()
print("Generated Password:", generated_password)