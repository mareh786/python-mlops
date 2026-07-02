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
    landing_page()
    ip = int(input("Enter your choice: "))

    #Checking the Inputs
    if ip == 1:
        vistorAdd()
        # print("Please enter the Details")
        # in_name =input("Please enter the name: ")
        # in_age = int(input("Please enter the age: "))
        # print(f"Details added successfully, Welcome {in_name}...")
    elif ip == 2:
        visitorDel()
        # print("Provide the name and age of the visitor")
        # out_name =input("Please enter the name: ")
        # out_age = int(input("Please enter the age: "))
        # print(f"Thanks for visiting {out_name}")
    elif ip == 3:
        visitorList()
    elif ip == 4:
        programExit()
    
    else:
        print("Kindly enter a valid choice!!!")
        landing_page()

def visitorAdd(): 
    print("Adding Visitor!!!")
def visitorDel():
    print("Visitor removed!!!")
def visitorList():
    print("Visitor checking!!!")
def programExit():
    print("Thanks for choosing us!!!")
    exit
