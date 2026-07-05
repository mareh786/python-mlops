# Find Most frequent Element
lst= [1,2,3,4,5,5,4,4,3,3,3,2,1]

freq = {}
for ch in lst: 
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
for key, value in freq.items:
    print(key, 3)
print(freq)
print(max(freq.values()))