from tkinter import *
from tkhtmlview import HTMLLabel
import webbrowser

root = Tk()
root.geometry("400x100")
room = IntVar()




def clicked(value):
	myLabel = Label(root, text=room.get())
	if room.get() == 1:
#case 1 if blue
		f = open('blue.html','w')
		message = """<html><head><link rel="stylesheet" href="Style.css"></head><body><h1 style ="color:blue;">Happy Birthday</h1><video autoplay muted loop id="myVideo"><source src="movie.mp4" type="video/mp4">Video not found</video><div class="innertext">""" + e.get() + """</div></body></html>"""
		f.write(message)
		f.close()
		webbrowser.open_new_tab('blue.html')
#case 2 if red
	elif room.get() == 2:
		f = open('red.html','w')
		message = """<html><head><link rel="stylesheet" href="Style1.css"></head><body><h1 style ="color:red;">Happy Birthday</h1><video autoplay muted loop id="myVideo"><source src="movie.mp4" type="video/mp4">Video not found</video><div class="innertext">""" + e.get() + """</div></body></html>"""
		f.write(message)
		f.close()
		webbrowser.open_new_tab('red.html')
#case 3 if yellow
	elif room.get() == 3:
		f = open('yellow.html','w')
		message = """<html><head><link rel="stylesheet" href="Style2.css"></head><body><h1 style ="color:yellow;">Happy Birthday</h1><video autoplay muted loop id="myVideo"><source src="movie.mp4" type="video/mp4">Video not found</video><div class="innertext">""" + e.get() + """</div></body></html>"""
		f.write(message)
		f.close()
		webbrowser.open_new_tab('yellow.html')
#case 4 if orange
	elif room.get() == 4:
		f = open('orange.html','w')
		message = """<html><head><link rel="stylesheet" href="Style3.css"></head><body><h1 style ="color:orange;">Happy Birthday</h1><video autoplay muted loop id="myVideo"><source src="movie.mp4" type="video/mp4">Video not found</video><div class="innertext">""" + e.get() + """</div></body></html>"""
		f.write(message)
		f.close()
		webbrowser.open_new_tab('orange.html')

Radiobutton(root, text="Blue", variable=room, value=1).pack(side=LEFT)
Radiobutton(root, text="Red", variable=room, value=2).pack(side=LEFT)
Radiobutton(root, text="Yellow", variable=room, value=3).pack(side=LEFT)
Radiobutton(root, text="Orange", variable=room, value=4).pack(side=LEFT)


e = Entry(root, width=15)
e.pack(ipady=8)

myButton = Button(root, text="Make A Party", command=lambda: clicked(room.get()))
myButton.pack(side=TOP)


root.mainloop()