# #Count Words in a Sentence

# sent = "I love Python"

# sp = sent.split()

# print(sp)

# count = 0
# for x in sp:
#     count +=1
    
# print(count)

def func(sentence):
    a = sentence.split()
    count = 0
    for x in a:
        count+=1
    return count
value =func("I love Muhammad")
print(f"The word count in the given string is {value}")