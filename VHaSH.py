from tkinter import filedialog
from tkinter import *
import hashlib

window = Tk()
window.geometry("865x185")

Title = window.title("VHaSH")

path = StringVar()
val = StringVar()
val2 = StringVar()
val3 = StringVar()
val4 = StringVar()

def openFile():
	global input_file
	input_file =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes=[("All Files","*.*")])
	path.set(input_file)
	calculate()
	
def calculate():
	md5 = hashlib.md5()
	sha1 = hashlib.sha1()
	sha256 = hashlib.sha256()
	sha512 = hashlib.sha512()

	file = open(input_file, 'rb') 
	data = file.read()
	sha256.update(data)
	md5.update(data)
	sha1.update(data)

	val.set(md5.hexdigest().upper())
	val2.set(sha1.hexdigest().upper())
	val3.set(sha256.hexdigest().upper())
	val4.set(sha512.hexdigest().upper())
	

def main():	
	s = LabelFrame(window,text="Generate Hash")
	s.grid(row=0, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
	Label(s,text="File:",fg = "red").grid(row=0)
	Label(s,text="MD5:",fg = "green").grid(row=1)
	Label(s,text="SHA1:",fg = "green").grid(row=2)
	Label(s,text="SHA256:",fg = "green").grid(row=3)
	Label(s,text="SHA512:",fg = "green").grid(row=4)
	
	e1 = Entry(s,width=80,textvariable=path)
	e2 = Entry(s,width=80,textvariable=val)
	e3 = Entry(s,width=80,textvariable=val2)
	e4 = Entry(s,width=80,textvariable=val3)
	e5 = Entry(s,width=80,textvariable=val4)
	
	e1.grid(row=0,column=1)
	Button(s,text="Browse&Generate",fg = "blue",command=openFile).grid(row=0,column=2)
	e2.grid(row=1,column=1)
	Button(s,text="Copy MD5",command= lambda:copy(val)).grid(row=1,column=2)
	e3.grid(row=2,column=1)
	Button(s,text="Copy SHA1",command= lambda:copy(val2)).grid(row=2,column=2)
	e4.grid(row=3,column=1)	
	Button(s,text="Copy SHA256",command= lambda:copy(val3)).grid(row=3,column=2)
	e5.grid(row=4,column=1)	
	Button(s,text="Copy SHA512",command= lambda:copy(val4)).grid(row=4,column=2)
	
def copy(item):
	window.clipboard_clear()  
	window.clipboard_append(item.get())  

main()
window.mainloop()


