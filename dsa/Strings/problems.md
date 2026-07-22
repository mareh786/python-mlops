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
