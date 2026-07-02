# Problem 2: Character Frequency

def checkFreq(char, target):
    count = 0
    for letter in char:
        if letter == target:
            count+= 1
    return count


value = checkFreq("banana", "a")

if value == 0:
    print("The character is not found")
else:
    print("The occurence of the choosen char is ", value)