import sys

if len(sys.argv) < 2:
    sys.exit(1)

original = sys.argv[1]   
reversed_input = original[::-1]

print("The reversed value is =", reversed_input)

if original == reversed_input:
    print("It is a palindrome")
else:
    print("It is not a palindrome")