# define a matrix
matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]
# print the whole matrix
print(matrix)
# print first element
print(matrix[1])
# print the first element of the zeroth list
print(matrix[0][1])
# use a for loop to print each element individually
for rows in matrix:
	for each in rows:
		print(each)