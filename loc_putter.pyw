#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file1 = filedialog.askopenfilename()

eng = file1.split('/')[-1]
rus = 'rus_' + eng
neweng = 'new_' + eng
file2 = file1.replace(eng, rus)
file3 = file1.replace(eng, neweng)
loc = open(file1, 'r', encoding='utf-8')
newloc = open(file2, 'r', encoding='utf-8')
itog = open(file3, 'w', encoding='utf-8')

i = -1
trlist=[]
nonlist=[]

for line in newloc:
	trlist.append(line.rstrip())

for line in loc:
	nonlist.append(line.rstrip())
	i+= 1
	if ((line.find (': ') > 0) or (line.find (':0 ') > 0) or (line.find (':1 ') > 0)) and (line[1] != '#'):
		a = line.find('"')
		curstr = line[0:a+1] + trlist[i] + '"'
	else:
		curstr = nonlist[i]
	itog.write(curstr + '\n')


loc.close()
newloc.close()
itog.close()