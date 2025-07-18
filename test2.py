class City:
    def __init__(self, name, country, population):
        self.name = name
        self.country = country
        self.population = population

    def display_info(self):
        print(f"City: {self.name}, Country: {self.country}, Population: {self.population}")

# Creating multiple City objects
# city1 = City("New York", "USA", 8419000)
# city2 = City("Tokyo", "Japan", 13960000)
# city3 = City("Paris", "France", 2148000)

# Printing information for each city
# city1.display_info()
# city2.display_info()
# Taking input from the user for a new city
# name = input("Enter city name: ")
# country = input("Enter country: ")
# population = int(input("Enter population: "))
# city1 = City(name, country, population)
# city1.display_info()
cities = [
    City("New York", "USA", 8419000),
    City("Tokyo", "Japan", 13960000),
    City("Paris", "France", 2148000),
    City("New York", "USA", 8419000),
    City("Tokyo", "Japan", 13960000),
    City("Paris", "France", 2148000),
    City("New York", "USA", 8419000),
    City("Tokyo", "Japan", 13960000),
    City("Paris", "France", 2148000),
    City("New York", "USA", 8419000),
    City("Tokyo", "Japan", 13960000),
    City("Paris", "France", 2148000),
    City("New York", "USA", 8419000),
    City("Tokyo", "Japan", 13960000),
    City("Paris", "France", 2148000),
    
]

for city in cities:
    city.display_info()