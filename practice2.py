# find the largest number in a list

# define list
nums = [3, 41, 12, 9, 74, 15]
# define variable to store the number
high_num = 0
# for loop to iterate over a list to find the highest number
for number in nums:
	# compare each individual number to the current highest number
	if number > high_num:
		# assign the current number as the highest number
		high_num = number
# print highest number
print(f"The largest number is: {high_num}")