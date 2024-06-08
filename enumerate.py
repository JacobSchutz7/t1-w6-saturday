# define list
animals = ["cat", "dog", "rabbit", "horse"]
# for loop to iterate and enumerate over the list. the first value will index the elements, the second is the data to be iterated over
for index, animal in enumerate(animals):
	print(index, animal)

# find the index of the cherry in a list of fruits

# define list of fruits
fruits = ["apple", "banana", "cherry"]
# for loop to iterate through fruits
for index, fruit in enumerate(fruits):
	# check if the current element is the cherry
	if fruit == "cherry":
		# print the index
		print(f"The cheery is at element {index}")
		# to end the loop after we have found the cherry! 
		break