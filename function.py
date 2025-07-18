#function in python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
print(add(3, 5))  # Output: 8

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b    
print(multiply(4, 5))  # Output: 20

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b    
print(subtract(10, 4))  # Output: 6

def divide(a, b):
    """Returns the quotient of a and b."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b    
print(divide(20, 4))  # Output: 5.0

# Function with default parameters
def my_function(fname):
  print(fname + " Pradhan")

my_function("Soleil")
my_function("Ram")
my_function("Shyam")
 
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Indexing in function arguments
def my_function(*kids): 
  print("The youngest child is " + kids[2])

  my_function("ram", "sita", "Hari")

# Function with keyword arguments
def my_function(child3, child2, child1):    
  print("The youngest child is " + child3) 
  print("The middle child is " + child2)
  print("The oldest child is " + child1) 
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
  

