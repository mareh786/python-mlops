
# Function to check whether two strings are anagrams
def is_anagram(str1, str2):
    # Check if both strings have the same length
    if len(str1) != len(str2):
        return "The strings are not anagrams!"

    # Convert both strings to lowercase, sort them, and compare
    elif sorted(str1.lower()) == sorted(str2.lower()):
        return "The strings are anagrams."

    # If the sorted strings are different, they are not anagrams
    else:
        return "The strings are not anagrams."


# Example
print(is_anagram("adile", "adiil"))


# ----------------------------------------
# Alternative approach (step-by-step)
# ----------------------------------------

# str1 = "acebd"
# str2 = "abcde"

# # Convert strings to lowercase lists
# s = list(str1.lower())
# t = list(str2.lower())

# # Sort both lists
# s.sort()
# t.sort()

# # Print sorted lists
# print(s)
# print(t)

# # Compare the sorted lists
# if s == t:
#     print(True)
# else:
#     print(False)
