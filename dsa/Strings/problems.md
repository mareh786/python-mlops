# Strings

## Problem 1: Toggle Case

Convert every uppercase letter to lowercase and every lowercase letter to uppercase.

### Example

```python
toggle_case("PyThOn123")
```

Output:

```text
pYtHoN123
```

### Concepts

- ASCII values
- Character traversal

---

## Problem 2: Check if One String is a Rotation of Another

Return `True` if one string is a rotation of the other.

### Example

```python
is_rotation("ABCD", "CDAB")
```

Output:

```text
True
```

### Concepts

- String manipulation
- Pattern recognition

---

## Problem 3: Find the Longest Common Prefix

Given a list of strings, return the longest common prefix.

### Example

```python
longest_common_prefix(["flower", "flow", "flight"])
```

Output:

```text
"fl"
```

### Concepts

- String comparison
- Traversal

---

## Problem 4: Check if Two Strings Differ by Exactly One Character

Return `True` if two strings have the same length and differ at exactly one position.

### Example

```python
one_char_difference("cat", "cut")
```

Output:

```text
True
```

### Concepts

- Character comparison
- Traversal

---

## Problem 5: Remove Consecutive Duplicate Characters

Remove consecutive duplicate characters while keeping one occurrence.

### Example

```python
remove_consecutive_duplicates("aaabbccdaa")
```

Output:

```text
abcda
```

### Concepts

- Traversal
- String construction

---

## Problem 6: Find the Most Frequent Character

Return the character that appears the most.

Assume there is only one correct answer.

### Example

```python
most_frequent("programming")
```

Output:

```text
g
```

### Concepts

- Hashing
- Frequency counting

---

## Problem 7: Check if a String is a Subsequence of Another

Return `True` if the first string is a subsequence of the second.

### Example

```python
is_subsequence("ace", "abcde")
```

Output:

```text
True
```

### Concepts

- Two pointers (intro)
- Traversal

---

## Problem 8: Find the First Repeating Character

Return the first character that repeats in the string.

### Example

```python
first_repeating("abcaef")
```

Output:

```text
a
```

### Concepts

- Hashing
- Traversal

---

## Problem 9: Check if Two Strings are Isomorphic

Two strings are isomorphic if characters from one string can be replaced to get the other.

### Example

```python
is_isomorphic("egg", "add")
```

Output:

```text
True
```

### Concepts

- Mapping
- Hashing

---

## Problem 10: Reverse the Order of Words

Reverse the order of words in a sentence without reversing the characters of each word.

### Example

```python
reverse_words("I love Python")
```

Output:

```text
Python love I
```

### Concepts

- Strings
- Split
- Traversal

# Strings

## Problem 11: Check if Two Strings are One Edit Away

Two strings are one edit away if you can make them equal by performing **exactly one** of the following operations:

- Insert one character
- Delete one character
- Replace one character

### Example

```python
one_edit_away("pale", "ple")
```

Output:

```text
True
```

### Concepts

- Two Pointers
- String Comparison
- Edge Cases

---

## Problem 12: Longest Substring Without Repeating Characters

Return the length of the longest substring containing unique characters.

### Example

```python
longest_unique_substring("abcabcbb")
```

Output:

```text
3
```

### Concepts

- Sliding Window (Introduction)
- Hash Set
- Two Pointers

---

## Problem 13: Group Anagrams

Given a list of strings, group all anagrams together.

### Example

```python
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
```

Output:

```text
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

### Concepts

- Hash Map
- Sorting
- Grouping

---

## Problem 14: Find the Longest Palindromic Prefix

Return the longest prefix of the string that is also a palindrome.

### Example

```python
longest_palindromic_prefix("levelup")
```

Output:

```text
"level"
```

### Concepts

- Strings
- Palindrome
- Prefix

---

## Problem 15: Decode a Compressed String

Given a compressed string where each character is followed by its count, expand it.

### Example

```python
decode("a3b2c4")
```

Output:

```text
"aaabbcccc"
```

### Concepts

- String Parsing
- Traversal
- String Construction

---

## Problem 16: Find the Smallest Window Containing a Character

Given a string and a character, return the length of the smallest substring containing that character.

### Example

```python
smallest_window("abcaad", "c")
```

Output:

```text
1
```

### Concepts

- Traversal
- Window Thinking

---

## Problem 17: Check if Two Strings are Mirror Images

Two strings are mirrors if one is the reverse of the other.

Do not use slicing (`[::-1]`) or `reversed()`.

### Example

```python
mirror("abcde", "edcba")
```

Output:

```text
True
```

### Concepts

- Two Pointers
- String Comparison

---

## Problem 18: Find the Character with Maximum Consecutive Occurrences

Return the character that has the longest consecutive run.

### Example

```python
max_consecutive_char("aaabbccccdde")
```

Output:

```text
"c"
```

### Concepts

- Traversal
- Consecutive Counting

---

## Problem 19: Check if a String Can Become a Palindrome by Removing One Character

Return `True` if removing at most one character makes the string a palindrome.

### Example

```python
valid_palindrome("abca")
```

Output:

```text
True
```

### Concepts

- Two Pointers
- Greedy Thinking

---

## Problem 20: String to Integer (atoi)

Implement a simplified version of `atoi`.

Rules:

- Ignore leading spaces.
- Handle optional '+' or '-'.
- Stop reading when a non-digit character is found.

### Example

```python
my_atoi("   -123abc")
```

Output:

```text
-123
```

### Concepts

- String Parsing
- Edge Cases
- Character Processing
