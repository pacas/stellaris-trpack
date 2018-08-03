#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file1 = filedialog.askopenfilename()

eng = file1.split('/')[-1]
rus = 'rus_' + eng
file2 = file1.replace(eng, rus)
loc = open(file1, 'r', encoding='utf-8')
newloc = open(file2, 'w', encoding='utf-8')

for line in loc:
	if (line.find (': ') > 0) or (line.find (':0') > 0) or (line.find (':1') > 0):
		if line[1] != '#':
			a = line.find('"')
			lt = line[a+1:-2]
			newloc.write(lt+ '\n')
		else:
			newloc.write('\n')
	else:
		newloc.write('\n')
loc.close()
newloc.close()