cities=["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

def print_cities(cities):
    for idx, city in enumerate(cities, 1):
        print(f"{idx}. {city}")
#print_cities(cities)      

def myfunction( cities):
        for idx, city in enumerate(cities, 1):
            city = city.upper()
            print(f"{idx}. {city}")
print(myfunction(cities))            


#def count_cities(cities):
 #    for idx, city in enumerate(cities,1):
 #         city=city.upper()
#          print(f"{idx}. {city}")
#print(count_cities(cities))         