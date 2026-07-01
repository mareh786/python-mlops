# Problem 2: Count Positive Numbers

def func(nums):
    count = 0
    for i in nums:
        if i > 0:
            count+=1
    return count
print(func([-2, 5, 0, 8, -1, 3]))