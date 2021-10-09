
def ahk_shitlist():
	"""
	ahk does not take kindly to some special charcters, so we need to escape them with "`"
	"""
	return [";"]

def _sanitizing(final_array):
	for index, i in enumerate(final_array):
		if i in ahk_shitlist():
			final_array[index] = "`"+i
	return final_array

def ahk_sanitizer(final_array):
	return _sanitizing(final_array)

def main():
	pass

if __name__ == "__main__":
	main()