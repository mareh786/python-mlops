def landing_page():
    print("_____VISITOR ENTRY REGISTER______")
    print("Choose any of the options below")
    print("*Menu*")
    print("1. Check in visitor")
    print("2. Check out visitor")
    print("3. View Current Visitors")
    print("4. Exit")


# Taking Input
def takeIP():
    ip = int(input("Enter your choice: "))

    #Checking the Inputs
    if ip == 1:
        print("Please enter the Details")
        in_name =input("Please enter the name: ")
        in_age = int(input("Please enter the age: "))
        print(f"Details added successfully, Welcome {in_name}...")
    elif ip == 2:
        print("Provide the name and age of the visitor")
        out_name =input("Please enter the name: ")
        out_age = int(input("Please enter the age: "))
        print(f"Thanks for visiting {out_name}")

