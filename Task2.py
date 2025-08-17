import random
import string
def gen_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
def show_menu():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        if length <  4:
            print("Invalid length. Please enter a number between 0 and 4.")
            return 
        password = gen_password(length)
        print(f"Generated password: {password}")  
        print(password)
    except ValueError:
        print("Invalid input. Please enter a valid number.")    
if __name__ == "__main__":
    show_menu()