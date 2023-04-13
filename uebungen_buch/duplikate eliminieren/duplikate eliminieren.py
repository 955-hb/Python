cities = ["Berlin", "München", "Amsterdam", "Stuttgart", "Berlin",
          "New York", "Berlin", "Stuttgart", "Moskau", "Hamburg",
          "Bremen", "Moskau", "Hamburg", "Bremen", "Moskau", "Stuttgart"]

cities_as_a_set = set(cities)

cities_back_to_list = list(cities_as_a_set)

cities_back_to_list.sort()

print(cities_back_to_list)

