def is_palindrome_pointer(s):
    s = str(s).lower()
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

# 1. Get input from the user
user_input = input("Enter a word or number to check: ")

# 2. Check and print the result
if is_palindrome_pointer(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is NOT a palindrome.")