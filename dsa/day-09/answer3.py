# Print the sentence in reverse order

def reverse_string(sentence):
    lst = sentence.split()
    reversed_lst = lst[::-1]
    reversed_str = " ".join(reversed_lst)
    return reversed_str

print(reverse_string("Reverse this sentence"))
