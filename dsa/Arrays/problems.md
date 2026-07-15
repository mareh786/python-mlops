# Arrays 

## Problem 1: Find the Maximum Element

Write a function that returns the largest element in an array.

### Example

```python
find_max([5, 9, 2, 7])
```

Output:

```text
9
```

---

## Problem 2: Reverse an Array

Return a new array with the elements in reverse order.

Do not use Python's built-in `reverse()` or slicing (`[::-1]`).

### Example

```python
reverse_array([1, 2, 3, 4])
```

Output:

```text
[4, 3, 2, 1]
```

---

## Problem 3: Check if an Array is Sorted

Return `True` if the array is sorted in non-decreasing order; otherwise return `False`.

### Example

```python
is_sorted([1, 2, 2, 5])
```

Output:

```text
True
```

Example

```python
is_sorted([3, 1, 2])
```

Output:

```text
False
```
## Problem 4: Linear Search

Write a function that returns the index of a target element in an array.

Return `-1` if the element is not found.

### Example

```python
linear_search([4, 7, 2, 9], 2)
```

Output:

```text
2
```

### Concepts

- Array traversal
- Searching
- Early exit

---

## Problem 5: Count Occurrences of an Element

Write a function that counts how many times a target element appears in an array.

### Example

```python
count_occurrences([1, 2, 2, 3, 2, 4], 2)
```

Output:

```text
3
```

### Concepts

- Traversal
- Counting
- Condition checking

---

## Problem 6: Find the Minimum Element

Write a function that returns the smallest element in an array.

### Example

```python
find_min([8, 3, 10, 1, 5])
```

Output:

```text
1
```

### Concepts

- Running minimum
- Array traversal
- Comparison


## Problem 7: Find the First Occurrence

Write a function that returns the index of the first occurrence of a target element in an array.

Return `-1` if the element is not found.

### Example

```python
first_occurrence([5, 2, 7, 2, 9], 2)
```

Output:

```text
1
```

### Concepts

- Linear Search
- Early Exit
- Array Traversal

---

## Problem 8: Find the Last Occurrence

Write a function that returns the index of the last occurrence of a target element in an array.

Return `-1` if the element is not found.

### Example

```python
last_occurrence([5, 2, 7, 2, 9], 2)
```

Output:

```text
3
```

### Concepts

- Traversal
- Indexing

---

## Problem 9: Count Even and Odd Numbers

Write a function that returns the count of even numbers and odd numbers in an array.

### Example

```python
count_even_odd([1, 2, 3, 4, 5, 6])
```

Output:

```text
(3, 3)
```

### Concepts

- Counting
- Conditions
- Traversal

## Problem 10: Find the Difference Between Maximum and Minimum

Write a function that returns the difference between the largest and smallest element in an array.

### Example

```python
difference([8, 2, 10, 5])
```

Output:

```text
8
```

---

## Problem 11: Second Largest Element

Write a function that returns the second largest **distinct** element in an array.

Return `None` if it doesn't exist.

### Example

```python
second_largest([10, 5, 20, 15])
```

Output:

```text
15
```

---

## Problem 12: Second Smallest Element

Write a function that returns the second smallest **distinct** element in an array.

Return `None` if it doesn't exist.

### Example

```python
second_smallest([8, 2, 5, 1, 3])
```

Output:

```text
2
```

## Problem 13: Move All Zeros to the End

Maintain the relative order of the non-zero elements.

### Example

```python
move_zeros([0, 1, 0, 3, 12])
```

Output:

```text
[1, 3, 12, 0, 0]
```

---

## Problem 14: Separate Even and Odd Numbers

Return a new array with all even numbers first, followed by all odd numbers.

Maintain the relative order.

### Example

```python
separate_even_odd([5, 2, 8, 1, 6, 3])
```

Output:

```text
[2, 8, 6, 5, 1, 3]
```

---

## Problem 15: Remove Duplicates from an Array

Return a new array containing only the first occurrence of each element.

### Example

```python
remove_duplicates([1, 2, 2, 3, 1, 4])
```

Output:

```text
[1, 2, 3, 4]
```

