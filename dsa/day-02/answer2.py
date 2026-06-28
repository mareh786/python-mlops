def maxNum():
    list1=['111', '192', '333', '414']
    
    
    maxnum= int(list1[0])
    
    for num in  list1:
        current_num = int(num)
        if current_num > maxnum:
            maxnum = current_num
            
    return maxnum

print(maxNum())