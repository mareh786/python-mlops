def landing_page():
    print("_____VISITOR ENTRY REGISTER______")
    print("Choose any of the options below")
    print("*Menu*")
    print("1. Check in visitor")
    print("2. Check out visitor")
    print("3. View Current Visitors")
    print("4. Exit")


# Taking Input
def take_input():
    landing_page()
    try:
        ip = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number. ")
    #Checking the Inputs
    if ip == 1:
        visitor_add()
    elif ip == 2:
        visitor_del()
    elif ip == 3:
        visitor_list()
    elif ip == 4:
        program_exit()
    
    else:
        print("Kindly enter a valid choice!!!")
        landing_page()

def visitor_add(): 
    print("Adding Visitor!!!")
def visitor_del():
    print("Visitor removed!!!")
def visitor_list():
    print("Visitor checking!!!")
def program_exit():
    print("Thanks for choosing us!!!")
    exit()
while True:
    take_input()