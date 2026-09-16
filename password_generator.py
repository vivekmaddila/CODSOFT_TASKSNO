

import random
import string


def generate_password():
    print("==============================")
    print("      PASSWORD GENERATOR")
    print("==============================")

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("❌ Password length must be greater than 0.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))

        print("\n------------------------------")
        print("Generated Password:")
        print(password)
        print("------------------------------")

    except ValueError:
        print("❌ Please enter a valid number.")


generate_password()