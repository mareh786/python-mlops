# Function to count the frequency of each character
def sec_freq_chars(text):
    freq = {}

    # Loop through each character in the string
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Return the frequency dictionary
    return freq


# Input string
val = sec_freq_chars("aaabbbbcccccdd")

# Print the frequency of each character
print("Character Frequencies:", val)

# Get all unique frequency values and sort them in descending order
all_values = sorted(set(val.values()), reverse=True)
print("Sorted Frequencies:", all_values)

# Find the second highest frequency
sec_max_freq = all_values[1]

# Store characters with the second highest frequency
result = []

# Loop through the frequency dictionary
for ch, count in val.items():
    if count == sec_max_freq:
        result.append(ch)

# Print the result
print("Second Most Frequent Character(s):", result)
