from _give_layout import give_layout, give_special_char, alphabet, special_char
from _ahk_sanitizer import ahk_sanitizer

def main():
	layout_alpha = give_layout()
	layout_special = give_special_char()

	alpha = alphabet()
	spec = special_char()

	# for ahk, special characters need escape "`"
	layout_alpha = ahk_sanitizer(layout_alpha)
	layout_special = ahk_sanitizer(layout_special)

	ahk_lines_alpha = [f'{j}::{i}\n' for i, j in zip(layout_alpha, alpha) if i != j]
	ahk_lines_special = [f'{j}::{i}\n' for i, j in zip(layout_special, spec) if i != j]

	with open("unurkey.ahk", "w+") as f:
		f.writelines(ahk_lines_alpha)
		f.writelines(ahk_lines_special)


if __name__ == "__main__":
	main()