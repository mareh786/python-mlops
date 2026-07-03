# Problem 2: Find the First Non-Repeating Character

char = "AAdDIIL"
s = char.lower()
for i in s:
    # print(i)
    if s.count(i) == 1:
        print("First non-repeating character:", i)
        break