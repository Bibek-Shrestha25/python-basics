def is_palindrome_number(n):
    original = str(n)
    reversed_num = original[::-1]
    return original == reversed_num

# Example usage:
num = int(input("Enter a number: "))
if is_palindrome_number(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")