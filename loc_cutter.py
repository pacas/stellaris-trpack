import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

eng = file_path.split('/')[-1]
rus = 'rus_' + eng

loc = open(eng, 'r', encoding='utf-8')
newloc = open(rus, 'w', encoding='utf-8')
for line in loc:
	if (line.find (': ') > 0) or (line.find (':0 ') > 0) or (line.find (':1 ') > 0):
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