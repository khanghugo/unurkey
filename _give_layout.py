from _ahk_sanitizer import ahk_shitlist

def _give_layout():
	reference = "the quick brown fox jumps over the lazy dog"
	print("Please type this like how you do in your layout with QWERTY: \n" + reference)

	while True:
		quote = input()
		if len(quote) != len(reference):
			print("I think you type it wrong. Try again.")
		else:
			break

	quote = quote.replace(" ", "")
	# or [i for i in quote], lol
	return [quote[0], quote[1], quote[2], quote[3], quote[4], quote[5], quote[6], quote[7], quote[8], quote[9], quote[10], quote[11], quote[12], quote[13], quote[14], quote[15], quote[16], quote[17], quote[18], quote[19], quote[20], quote[21], quote[22], quote[23], quote[24], quote[25], quote[26], quote[27], quote[28], quote[29], quote[30], quote[31], quote[32], quote[33], quote[34], ]

def _sort_layout(_give_layout_return):
	"""
	as you see, the _give_layout is still pretty primitive, i can try to make this one so code can be scable with a different panagram but anyway, it is just here
	to take in unfiltered data
	"""
	
	quote = ["t", "h", "e", "q", "u", "i", "c", "k", "b", "r", "o", "w", "n", "f", "o", "x", "j", "u", "m", "p", "s", "o", "v", "e", "r", "t", "h", "e", "l", "a", "z", "y", "d", "o", "g", ]
	# this will sort the userinput with the order of the above quote, so at least it can look prettier
	# i seriously can just do simpler things so there is no need for these long lists but anyway
	quote, _give_layout_return_sorted = (list(t) for t in zip(*sorted(zip(quote, _give_layout_return))))
	_give_layout_return_sorted_unduplicated = list(dict.fromkeys(_give_layout_return_sorted))

	return _give_layout_return_sorted_unduplicated

def _give_special_char():
	reference = ",./;'[]\\"
	print("\nProceed with the same for special keys: \n" + reference + " comma period backslash colon quote open close frontslash")

	while True:
		quote = input()
		if len(quote) != len(reference):
			print("I think you type it wrong. Try again.")
		else:
			break
	return [i for i in quote]

def alphabet():
	"""
	return a sorted list of alphabet characters
	"""
	return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def special_char():
	"""
	return a sorted special character list. sorted as in it is more convenient for qwerty like layout
	"""
	reference = ",./;'[]\\"
	reference_list = [i for i in reference]

	for index, i in enumerate(reference_list):
		if i in ahk_shitlist():
			reference_list[index] = "`"+i

	return reference_list

def give_special_char():
	return _give_special_char()

def give_layout():
	return _sort_layout(_give_layout())

def main():
	print(_sort_layout(_give_layout()))

if __name__ == "__main__":
	main()