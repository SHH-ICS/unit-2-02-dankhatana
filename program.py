# My Python Program
# Task:  Use the function myFunction to output a simple "Hello World!" statement

def myFunction(first_name):
    return "Hello, {}!".format(first_name)


first_name = input("Please enter your first name: ")

print(myFunction(first_name))
