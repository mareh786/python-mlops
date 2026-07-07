# Print the longest word in a sentence
def str_to_lst(sentence):
    lst = sentence.split()

    if len(lst) == 1:
        return lst[0]

    count_lst = []
    for word in lst:
        count_lst.append(len(word))

    longest_word_length = max(count_lst)

    for word in lst:
        if len(word) == longest_word_length:
            return word

value = str_to_lst("Python is an amazingg Language")
print(f"The longest word in the string is: {value}")
