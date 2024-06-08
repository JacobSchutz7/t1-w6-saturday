# skipping vowels in text
text = "Coder Academy"
vowels = "aeiouAEIOU"
# for loop to iterate over text
for each in text:
	# check if the current character is in the vowels string
	if each in vowels:
		continue
	print(each, end=" ")
print()

# coming from c++, "in" is fucking wild

# end a loop when iteration gets to "stop"
signals = ["start", "hold", "continue", "stop", "go"]
# for loop to iterate over signals
for signal in signals:
	if signal == "stop":
		break
	print(signal)