#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
import re


def search(subs, line):
	match = subs.search(line)
	if match is not None:
		return 1
	else:
		return 0


def main():
	root = tk.Tk()
	root.withdraw()
	file1 = filedialog.askopenfilename()
	eng = file1.split('/')[-1]
	rus = 'rus_' + eng
	file2 = file1.replace(eng, rus)
	loc = open(file1, 'r', encoding='utf-8')
	newloc = open(file2, 'w', encoding='utf-8')
	subs = re.compile(': |:0|:1|:"')

	for line in loc:
		if search(subs, line) == 1:
			if (line[0] and line[1]) != '#':
				a = line.find('"')
				lt = line[a + 1:-2]
				newloc.write(lt + '\n')
			else:
				newloc.write('\n')
		else:
			newloc.write('\n')
	loc.close()
	newloc.close()


if __name__ == "__main__":
	main()
