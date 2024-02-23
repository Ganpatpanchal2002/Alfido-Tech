import random
import string

def generate_password(length=12, include_special=True, include_numbers=True):
    characters = string.ascii_letters
    if include_special:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the length of the password: "))
    include_special = input("Include special characters? (yes/no): ").lower() == "yes"
    include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"

    password = generate_password(length, include_special, include_numbers)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
