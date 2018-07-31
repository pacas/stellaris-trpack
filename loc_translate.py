from googletrans import Translator
import tkinter as tk
from tkinter import filedialog
from langdetect import detect, DetectorFactory

root = tk.Tk()
root.withdraw()
DetectorFactory.seed = 0
translator = Translator()

file_path = filedialog.askopenfilename()
eng = file_path.split('/')[-1]
rus = 'tr_' + eng[4:]
loc = open(eng, 'r', encoding='utf-8')
itog = open(rus, 'w', encoding='utf-8')

i = 0
for line in loc:
	i += 1
	translation = ''
	print ("Строка ", i)
	if (len(line) > 2) and (line.find('§') == -1) and (line.find('$') == -1) and (line.find('£') == -1):
		test = detect(line)
		if test != 'ru':
			translation = translator.translate(line, dest='ru')
			translation = translation.text + '\n'
		else:
			translation = line
	else:
		translation = line
	itog.write(translation)