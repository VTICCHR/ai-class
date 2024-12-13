# example5.py
# This script demonstrates a simple greeting function with user input

def greet_user(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet_user(user_name))
