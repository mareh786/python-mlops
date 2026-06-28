def removeSpaces():
    str = "A d           I L            "
    newstr = ""
    for each in str:
        if each == ' ' :
            continue
        else:
            newstr+=each
            
    return newstr

finalstr = removeSpaces()

print(f"The final string is {finalstr}")