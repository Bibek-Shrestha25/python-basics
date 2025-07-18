def reverse_number(n):
    negative = n < 0
    n = abs(int(n))
    reversed_n = 0

    while n != 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10

    if negative:
        reversed_n = -reversed_n
    return reversed_n

num_str = input("Enter an integer: ")
try:
    num = int(num_str)
except ValueError:
    print("Invalid input.")
else:
    print(f"Reversed number: {reverse_number(num)}")


    # Another method using string slicing
    def reverse_number_str(n):
        negative = n < 0
        n_str = str(abs(int(n)))
        reversed_str = n_str[::-1]
        reversed_n = int(reversed_str)
        if negative:
            reversed_n = -reversed_n
        return reversed_n

    # Example usage
    try:
        # Try to convert the input string to an integer
        num = int(num_str)
    except ValueError:
        # If conversion fails, print an error message
        print("Invalid input.")
    else:
        # If conversion succeeds, print the reversed number using the string method
        print(f"Reversed number (string method): {reverse_number_str(num)}")
