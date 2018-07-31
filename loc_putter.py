import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

eng = file_path.split('/')[-1]
rus = 'rus_' + eng
neweng = 'new_' + eng

loc = open(eng, 'r', encoding='utf-8')
newloc = open(rus, 'r', encoding='utf-8')
itog = open(neweng, 'w', encoding='utf-8')

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