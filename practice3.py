# print a right angled triangle of stars

# define variable to use for iteration
stars = 5
# nested for loop to iterate using stars for range
for i in range(1, stars + 1):
	# a second for loop to print a star equal to the number of the current iteration
	for j in range(i):
		print("*", end = " ")
	# each iteration of the first loop prints a new line in order to create the triangle
	print()

# seems easier to use just one for loop for this? 
for i in range(6):
	print("* " * i, end = " ")
	print()