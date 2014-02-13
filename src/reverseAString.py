"""
Reverses a string.
"""
def reverseAString(string):
	string_length = len(string)
	i = 0
	product = []
	while i < string_length:
		product.append(string[string_length-1-i])
		i +=1
	return product

word = raw_input('Enter a word to reverse: \n')
print reverseAString(word)
