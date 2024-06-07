# create a list
countries = ["Australia", "New Zealand", "USA", "England"]
# print the whole list
print(countries)
# print specific element
print(countries[0])
# change an element
countries[1] = "South Africa"
# add a new element
countries.append("New Zealand")
# remove an element
countries.remove("USA")
# count number of items in the list
print(f"The number of countries in the tournament is: {len(countries)}")