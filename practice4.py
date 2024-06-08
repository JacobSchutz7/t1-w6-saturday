# count the occurence of a letter in the list

# define matrix
matrix = ["Coder", "Academy", "Champion"]
# define variable to store the number of occurences
count = 0
# for loop to iterate over the matrix
for word in matrix:
	for letter in word:
		if letter in "Cc":
			count += 1
# print the result
print(count)