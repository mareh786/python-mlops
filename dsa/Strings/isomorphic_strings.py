"""
---------------------------------------------------------
Program: Check if Two Strings are Isomorphic

Approach:
- Two strings are isomorphic if each character in the first
  string maps to exactly one character in the second string,
  and vice versa.
- If the lengths of the strings are different, they cannot
  be isomorphic.
- Use two dictionaries:
    - One to map characters from s1 to s2.
    - Another to map characters from s2 to s1.
- Traverse both strings simultaneously.
- If an existing mapping conflicts with the current character,
  return False.
- Otherwise, store the mapping.
- If all mappings are consistent, return True.

Time Complexity:
- Best Case: O(1)
  (Length mismatch.)

- Average Case: O(n)

- Worst Case: O(n)
  (Each character is processed exactly once.)

Space Complexity:
- O(n)
  (Two dictionaries are used to store character mappings.)

Key Learning:
- A one-to-one (bijective) mapping must exist between the
  characters of both strings.
- Using two hash maps ensures that no two characters map to
  the same character.
---------------------------------------------------------
"""


def is_isomorphic(s1, s2):
    # Strings of different lengths cannot be isomorphic
    if len(s1) != len(s2):
        return "Given strings can't be isomorphic"

    # Dictionaries to store mappings
    map_s1_s2 = {}
    map_s2_s1 = {}

    # Traverse both strings together
    for c1, c2 in zip(s1, s2):

        # Check if an existing mapping conflicts
        if ((c1 in map_s1_s2 and map_s1_s2[c1] != c2) or
                (c2 in map_s2_s1 and map_s2_s1[c2] != c1)):
            return False

        # Store the mapping
        map_s1_s2[c1] = c2
        map_s2_s1[c2] = c1

    return True


# Driver Code
print("Is Isomorphic:", is_isomorphic("add", "egg"))
