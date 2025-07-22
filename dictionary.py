myfamily = {
    "father": "John",   
    "mother": "Jane",
    "brother": "Mike",  
    "sister": "Emily",
    "grandfather": "Robert",
    "grandmother": "Linda"
}
print(myfamily)
# Function with variable-length arguments
def my_function(*family_members):
    for member in family_members:
        print("Family member: " + member)
my_function("John", "Jane", "Mike", "Emily", "Robert", "Linda")
# Function with keyword arguments
def my_function(**family_info):
    for role, name in family_info.items():
        print(role + ": " + name)   
my_function(father="John", mother="Jane", brother="Mike", sister="Emily", grandfather="Robert", grandmother="Linda")
# Function with default parameters
def my_function(family_member="Unknown"):
    print("Family member: " + family_member)
my_function("John")
my_function()  # Output: Family member: Unknown
# Function with variable-length arguments
def my_function(*args): 
    for arg in args:
        print("Argument: " + arg)
my_function("John", "Jane", "Mike", "Emily", "Robert", "Linda")
my_function("John", "Jane")  # Output: Argument: John, Argument: Jane
#Functin accessing dictionary values
def get_family_member(role):
    return myfamily.get(role, "Role not found") 
