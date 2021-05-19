def print_upper_case(words, letter_filter={}):
	""" Print a list of words in CAPS that meets all condition
	
	Args:
		words: A list of words
		letter_filter: optional, a set of letters to use as a filter for words printed
	"""

	for word in words:
		if word[0].lower() in letter_filter:
			print(word.upper())

print_upper_case(['hello', 'test', 'run', 'error'], {"a", "t"})