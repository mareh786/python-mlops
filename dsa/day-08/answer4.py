s = "The process of learning to code is a rewarding journey, but the process also comes with many challenges. When you encounter challenges while you code, you must remember that learning takes time. Every code error you fix makes you a better developer, so embrace the learning journey and enjoy the process."

# Counting words
# word_count = len(s.split())
# print(word_count)

# z = s.split()
# # print(z)
# dict = {}
# for word in z:
# dict[word]= dict.get(word, 0)+1
# print(dict)
def word_counter(str):
    lst = str.split()
    dict = {}
    for word in lst:
        dict[word] = dict.get(word, 0)+1
        
    return dict

print(word_counter("apple is only apple and apple in no banana"))
