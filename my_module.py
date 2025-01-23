# if __name__ == "__main__" --> it is used to determine whether a scripts is being run directly or imported as a module in another scripts
def greet(name):
    print(f"Hello, {name}")

if __name__ == "__main__":
     # This code runs only when the script is executed directly
    greet("Deepak")