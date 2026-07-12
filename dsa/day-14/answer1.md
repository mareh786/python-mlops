# Find the second most frequent character

def sec_freq_chars(str):
    freq = {}
    for ch in str:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

val = sec_freq_chars("aaabbbbcccccdd")

print(val)

all_values = sorted(set(val.values()), reverse=True)
print(all_values)

sec_max_freq = all_values[1]

result = []

for ch, count in val.items():
    if count == sec_max_freq:
        result.append(ch)

print(result)
