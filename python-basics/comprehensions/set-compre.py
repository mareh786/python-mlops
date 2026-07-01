# -------------------------------
# List: original data
# -------------------------------
alpha = ['a', 'b1', 'c', 'b1', 'a']
print(alpha)


# -------------------------------
# Set comprehension: remove duplicates
# -------------------------------
uniq = {x for x in alpha}   # creates a set → unique elements only
print(uniq)


# -------------------------------
# Filter elements containing "1"
# -------------------------------
moreuniq = {x for x in alpha if "1" in x}   # keeps only items with '1'
print(moreuniq)


# -------------------------------
# Removing duplicates from numbers
# -------------------------------
nums = [1, 2, 2, 3, 4, 4, 5]

unique_nums = {x for x in nums}   # convert list → set (removes duplicates)
print(unique_nums)


# -------------------------------
# Filter even numbers
# -------------------------------
even = {x for x in nums if x % 2 == 0}   # keep only even numbers
print(even)


# -------------------------------
# Filter words by length
# -------------------------------
words = ["apple", "bat", "car", "apple", "bat"]

longerWords = {x for x in words if len(x) > 3}   # words with length > 3
print(longerWords)


# -------------------------------
# Transform + filter (uppercase)
# -------------------------------
upperWords = {x.upper() for x in words if len(x) > 3}
# convert to uppercase only if length > 3
print(upperWords)


# -------------------------------
# Squares of numbers > 1
# -------------------------------
sqr = {x**2 for x in nums if x > 1}
# squares of numbers greater than 1
print(sqr)


# -------------------------------
# Squares of odd numbers
# -------------------------------
oddsqr = {x**2 for x in nums if x % 2 == 1}
# filter odd numbers → square them
print(oddsqr)