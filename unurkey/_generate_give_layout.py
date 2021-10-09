"""
this will help with scripting and stuff
overall, dev stuff
"""

quote_var_name = "quote"
suffix = "_key"
panagram = "the quick brown fox jumps over the lazy dog"
panagram_stripped = panagram.replace(" ", "")

def assigning():
	# yes, i use variable out of scope
	for index, i in enumerate(panagram_stripped):
		print(f'{i}{suffix} = {quote_var_name}[{index}]')
def reminding():
	for index, i in enumerate(panagram_stripped):
		print(f'{i}{index} ', end = "")
def listing():
	print("[", end="")
	for index, i in enumerate(panagram_stripped):
		print(f'{quote_var_name}[{index}], ', end="")
	print("]")
def panagram_listing():
	print("[", end="")
	for index, i in enumerate(panagram_stripped):
		print(f'"{i}", ', end="")
	print("]")
def alphabet_listing():
	l = sorted([i for i in panagram_stripped])
	print(l)
	
def main():
	alphabet_listing()
	pass



if __name__ == "__main__":
	main()
