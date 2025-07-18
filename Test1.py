# 9. Print multiplication table of a number
num = 6
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

    # Print triangle pattern of *
    rows = 10
    for i in range(1, rows + 1):
        print('*' * i)

        class Subtraction:
            def __init__(self, a, b):
                self.a = a
                self.b = b

            def subtract(self):
                return self.a - self.b

        class InheritedSubtraction(Subtraction):
            pass

        # Example usage
        obj = InheritedSubtraction(10, 4)
        print("Subtraction:", obj.subtract())

        # Dictionary with key-value pairs in a loop multiple times
        my_dict = {}
        for i in range(5):
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value
        print("Dictionary contents:", my_dict)
 
        # Function to check if a number is prime
        def is_prime(n):
 
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True 
        # Example usage
        number = 29 
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
