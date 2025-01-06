import random
import string

lowercase_letters = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = string.ascii_uppercase # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = string.digits                     # "0123456789"
special_characters = string.punctuation    # "!@#$%^&*()"

length = int(input("Enter the desired password length: "))

def generate_password(length):
    password = [] # List to store the generated password characters

     # Combine all the character pools
    pool = lowercase_letters + uppercase_letters + digits + special_characters

    # Randomly select characters from the pool and add them to the password list
    for i in range(length):
        password.append(random.choice(pool))

    random.shuffle(password)

    # Convert the password list to a string and return it
    return ''.join(password)


print(generate_password(length))