# Problem 2: Find the First Non-Repeating Character

char = "AAdDI IL"
s = char.lower()
s = s.replace(" ", "")
for i in s:
    if s.count(i) == 1:
        print("First non-repeating character:", i)
        break