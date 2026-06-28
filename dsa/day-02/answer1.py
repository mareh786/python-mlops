def isPalindrome():
    str = input("Enter the string: ")
    str = str
    if str.lower() == str[::-1].lower():
        print(f"The given string {str} is a Palindrome")
    else:
        print(f"The given string {str} is not a Palindrome")
        
isPalindrome()