# Function1: Placeholder function (currently does nothing)
def function1():
    pass  # 'pass' is used when a function is required syntactically but no logic is needed


# Function2: Responsible for taking user input
def function2():
    # Prompt user to enter their name
    name = input("Enter the name: ")
    
    # Prompt user to enter their age
    age = input("Enter your age: ")
    
    # Return the collected values so they can be used in other functions
    return name, age


# Function3: Responsible for displaying user details
def function3(name, age):
    # Print the values passed as arguments
    print(f"The user input was name= {name}, age= {age}")


# Main driver function
def runapp():
    # Infinite loop to keep the application running continuously
    while True:
        # Call placeholder function (currently no operation)
        function1()

        # Call function2 and store returned values
        name, age = function2()

        # Pass the stored values to function3 for display
        function3(name, age)


# Entry point of the program
runapp()