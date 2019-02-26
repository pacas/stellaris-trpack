#!/usr/bin/python3
from googletrans import Translator
import tkinter as tk
from tkinter import filedialog
from langdetect import detect, DetectorFactory


def search(subs, line):
	counter = 0
	for i in range(len(subs)):
		if subs[i] in line:
			counter += 1
	if counter != 0:
		return 1
	else:
		return 0


def main():
	root = tk.Tk()
	root.withdraw()
	DetectorFactory.seed = 0
	translator = Translator()

	file1 = filedialog.askopenfilename()
	eng = file1.split('/')[-1]
	rus = 'tr_' + eng[4:]
	file2 = file1.replace(eng, rus)
	loc = open(file1, 'r', encoding='utf-8')
	itog = open(file2, 'w', encoding='utf-8')
	subs = ['§', '$', '£']

	i = 0
	for line in loc:
		i += 1
		translation = ''
		if (len(line) > 2) and (search(subs, line) == 0):
			test = detect(line)
			if test != 'ru':
				translation = translator.translate(line, dest='ru')
				translation = translation.text + '\n'
			else:
				translation = line
		else:
			translation = line
		itog.write(translation)
	print('end')


if __name__ == "__main__":
	main()
