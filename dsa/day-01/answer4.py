# Approach 1
string= "adil"


print(string[ : :-1])

# Approach 2

def revStr():
    str = input("Enter the string: ")
    result = ""
    for i in range(len(str) -1, -1, -1):
        result += str[i]
        
    return result

print(revStr())