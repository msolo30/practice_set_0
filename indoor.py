def quite():
    name = input("What is your name? ").casefold() 
    hello(name)

def hello(user_name):
    print(f"Hello, {user_name}")

quite()