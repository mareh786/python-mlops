def searchFunc(nums, target):
    for i in nums:
        if i == target:
            return list.index(i)
        else:
            return -1

print(searchFunc([1, 2, 3, 4, 5], 5))