import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits

    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
   
    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    
    password = generate_password(length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()