# Problem 1: Find the Missing Number
def missingNum(nums):
    for i in range(1, len(nums)):
        if i not in nums:
            return i
            
    return i
value = missingNum([1, 2, 3, 5])

print(f"The missing number is {value}")