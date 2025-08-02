cities=["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

def print_cities(cities):
    for idx, city in enumerate(cities, 1):
        print(f"{idx}. {city}")
#print_cities(cities)      

#def myfunction( cities):
      #  for idx, city in enumerate(cities, 1):
       #     city = city.upper()
        #    print(f"{idx}. {city}")
##print(myfunction(cities))            


#def count_cities(cities):
 #    for idx, city in enumerate(cities,1):
 #         city=city.upper()
#          print(f"{idx}. {city}")
#print(count_cities(cities))         



#for idx, city in enumerate(cities, 1):
 #   print(f"{idx}. {city} (length: {len(city)})")

def check_length(cities):
     for idx, city in enumerate(cities,1):
         print(f"{idx}. {city} (length is: {len(city)}) and the type is: {type(city)}")

print( check_length(cities)); 

#tuples
my_tuple=("apple","mango","banana","melon","orange")

class FindFruit:
    def __init__(self, my_tuple):
        # Normalize all fruits to lowercase once
        self.my_tuple = tuple(f.lower() for f in my_tuple)

    def find_fruit(self, fruit):
        if not fruit or not isinstance(fruit, str):
            return "No fruit provided for search."
        fruit = fruit.lower()
        if fruit in self.my_tuple:
            return f"{fruit} is found in the tuple"
        else:
            return f"{fruit} is not found in the tuple"
       

# Example usage:
search_fruit = input("Enter the fruit to find: ")
print(FindFruit(my_tuple).find_fruit(search_fruit))

