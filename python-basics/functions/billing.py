from operator import add


def customerDetails():
    name= input("Enter the name: ")
    age= input("Enter your Age: ")
    mobNum= input("Enter your mobile number: ")
    return name, age, mobNum

name, age, mobNum = customerDetails()

def additems():
    items= []
    while True:
        itemName= input("Enter the name of Item: ")
        itemPrice= int(input("Enter the per unit cost: "))
        itemQuantity= int(input("Enter the units to but: "))
        itemTotal= itemPrice*itemQuantity
        item={ "item": itemName, "cost": itemPrice, "quantity": itemQuantity, "total": itemTotal}
        items.append(item)
        choice= input("Do you want to add more items? (y/n): ")
        if choice.lower != 'y':
            break

    return items


customerDetails()
additems()
def orderDetails():
# Creating the list of items & total amount    
    print("_________Final Bill__________")


def total_amount():
# Total amount after discount
    pass

def final_amount():
# Total after 18% GST
    pass

def printBill():
    # Create bill using customer details, Items, discount, tax and final total
    pass
