# Count Occurrences of a Character


def func(word, letter):
    count = 0
    for item in word:
        if item == letter:
            count+=1
        else: 
            continue
    return count

print(func("banaaaaaaana", "b"))