# Remove Duplicate characters from a String

def rem_duplicate(str): 
 new_str = "" 
 for ch in str: 
 if ch not in new_str: 
 new_str = new_str + ch 
 return new_str 
print(rem_duplicate("programming"))
