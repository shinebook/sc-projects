"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
DATA = []
times = 0
RESULT = []
Word_data = []


def main():
	"""
	TODO:
	"""
	read_dictionary()
	big_lst = []
	word_data = []
	q = 0
	for i in range(4):
		ch_lst = []
		a = input(f"{i+1} row of letters: ")
		a = a.lower()
		b = a.replace(" ", "")
		if len(a) == 7 and len(b) == 4 and b.isalpha() and len(a.strip()) == 7 and len(a.split()) == 4:
			for ch in b:
				ch_lst.append(ch)
			big_lst.append(ch_lst)
			q += 1
		else:
			print("Illegal input")
			break
	if q == 4:
		small_lst = remove_same(big_lst)
		# 去除不是board上開頭的字
		for letter in DATA:
			for ch in small_lst:
				if letter.startswith(ch):
					Word_data.append(letter)
		find_word(big_lst)
		print(f"There are {times} words in total.")


def find_word(big_lst):
	for i in range(len(big_lst[0])):
		for j in range(len(big_lst)):
			helper(big_lst, "", [], i, j)


def helper(big_lst, cur, lst, x_cord, y_cord):
	global times
	xy_cord = (x_cord, y_cord)
	if cur in Word_data and cur not in RESULT:
		RESULT.append(cur)
		print(f"Found {cur}")
		times += 1
		helper(big_lst, cur, lst, x_cord, y_cord)
	else:
		if xy_cord not in lst:
			# choose
			cur += big_lst[x_cord][y_cord]
			lst.append(xy_cord)
			if has_prefix(cur):
				# explore
				for i in range(-1, 2, 1):
					for j in range(-1, 2, 1):
						xxx = x_cord + i
						yyy = y_cord + j
						if 0 <= xxx < len(big_lst):
							if 0 <= yyy < len(big_lst[0]):
								helper(big_lst, cur, lst, xxx, yyy)
								# un-choose
			cur = cur[:-1]
			lst.pop()


def remove_same(a):
	b = []
	for i in a:
		for j in i:
			if j not in b:
				b.append(j)
	return b


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE) as data_set:
		for letter in data_set:
			if len(letter) > 4:
				DATA.append(letter.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in DATA:
		if i.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
