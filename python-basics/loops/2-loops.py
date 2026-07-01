# NOTE: This is actually a SET, not a list (because of {} brackets)
# Sets are unordered, so output order may change
list = {"1", "2", "3", "4", "5"}

# Loop through each element in the set
for time in list:
    # time will take values like "1", "2", etc. (order not guaranteed)
    
    # f-string is used to format the output nicely
    print(f"It's {time} O'clock")
