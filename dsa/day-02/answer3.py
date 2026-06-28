def consonant():
    str = "Mohammed"
    str = str.lower()
    count = 0
    for i in str:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            count+=1
            
    return count

consonants = consonant()

print(f"The number of consonants is the word is {consonants}")


    