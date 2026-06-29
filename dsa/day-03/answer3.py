# Square Every Number in a List

def sqr(list1):
    sqrlist = []
    for item in list1:
        item = int(item)
        sqrlist.append(item*item)
        
    return sqrlist
list0= ["2", '90', '8']

print(sqr(['9', '18', '27']))