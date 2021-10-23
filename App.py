from tkinter import *
from tkhtmlview import HTMLLabel
import webbrowser

root = Tk()
root.geometry("600x200")
room = IntVar()
room.set(1)
v = IntVar()
v.set(1)


def partyFunction(videoName):	
	if room.get() == 1:
	#case 1 if blue
		f = open('blue.html','w')
		message = """<html><head><link rel="stylesheet" href="Stylea.css"></head><body><img src="bg.png"><h1>""" + happy.get() + """</h1><video autoplay muted loop id="myVideo"><source src=""" + videoName + """ type="video/mp4">Video not found</video><div class="innertext">""" + e.get() + """</div></body></html>"""
		f.write(message)
		f.close()
		webbrowser.open_new_tab('blue.html')
	#case 2 if red
	elif room.get() == 2:
		f = open('red.html','w')
		message = """<html><head><link rel="stylesheet" href="Styleb.css"></head><body><img src="bg.png"><h1>""" + happy.get() + """</h1><video autoplay muted loop id="myVideo"><source src=""" + videoName + """ type="video/mp4">Video not found</video><div class="innertext">""" + e.get() + """</div></body></html>"""
		f.write(message)
		f.close()
		webbrowser.open_new_tab('red.html')
	#case 3 if yellow
	elif room.get() == 3:
		f = open('yellow.html','w')
		message = """<html><head><link rel="stylesheet" href="Stylec.css"></head><body><img src="bg.png"><h1>""" + happy.get() + """</h1><video autoplay muted loop id="myVideo"><source src=""" + videoName + """ type="video/mp4">Video not found</video><div class="innertext">""" + e.get() + """</div></body></html>"""
		f.write(message)
		f.close()
		webbrowser.open_new_tab('yellow.html')
	#case 4 if orange
	elif room.get() == 4:
		f = open('orange.html','w')
		message = """<html><head><link rel="stylesheet" href="Styled.css"></head><body><img src="bg.png"><h1>""" + happy.get() + """</h1><video autoplay muted loop id="myVideo"><source src=""" + videoName + """ type="video/mp4">Video not found</video><div class="innertext">""" + e.get() + """</div></body></html>"""
		f.write(message)
		f.close()
		webbrowser.open_new_tab('orange.html')

def oldFunction(videoName):	
	if room.get() == 1:
	#case 1 if blue
		f = open('blue.html','w')
		message = """<html><head><link rel="stylesheet" href="Style.css"></head><body><img src="bg.png"><h1>""" + happy.get() + """</h1><video autoplay muted loop id="myVideo"><source src=""" + videoName + """ type="video/mp4">Video not found</video><div class="innertext">""" + e.get() + """</div></body></html>"""
		f.write(message)
		f.close()
		webbrowser.open_new_tab('blue.html')
	#case 2 if red
	elif room.get() == 2:
		f = open('red.html','w')
		message = """<html><head><link rel="stylesheet" href="Style1.css"></head><body><img src="bg.png"><h1>""" + happy.get() + """</h1><video autoplay muted loop id="myVideo"><source src="movie.mp4" type="video/mp4">Video not found</video><div class="innertext">""" + e.get() + """</div></body></html>"""
		f.write(message)
		f.close()
		webbrowser.open_new_tab('red.html')
	#case 3 if yellow
	elif room.get() == 3:
		f = open('yellow.html','w')
		message = """<html><head><link rel="stylesheet" href="Style2.css"></head><body><img src="bg.png"><h1>""" + happy.get() + """</h1><video autoplay muted loop id="myVideo"><source src="movie.mp4" type="video/mp4">Video not found</video><div class="innertext">""" + e.get() + """</div></body></html>"""
		f.write(message)
		f.close()
		webbrowser.open_new_tab('yellow.html')
	#case 4 if orange
	elif room.get() == 4:
		f = open('orange.html','w')
		message = """<html><head><link rel="stylesheet" href="Style3.css"></head><body><img src="bg.png"><h1>""" + happy.get() + """</h1><video autoplay muted loop id="myVideo"><source src="movie.mp4" type="video/mp4">Video not found</video><div class="innertext">""" + e.get() + """</div></body></html>"""
		f.write(message)
		f.close()
		webbrowser.open_new_tab('orange.html')


def clicked(value):
	myLabel = Label(root, text=room.get())
	if v.get() == 2:
		videoName = "fortnite.mp4"
		partyFunction(videoName)
	elif v.get() == 3:
		videoName = "harry.mp4"
		partyFunction(videoName)
	elif v.get() == 4:
		videoName = "pokemon.mp4"
		partyFunction(videoName)
	elif v.get() == 5:
		videoName = "minecraft.mp4"
		partyFunction(videoName)
	elif v.get() == 1:
		videoName = "movie.mp4"
		oldFunction(videoName)
	
	

Radiobutton(root, text="Blue", variable=room, value=1).pack(side = "left")
Radiobutton(root, text="Red", variable=room, value=2).pack(side = "left")
Radiobutton(root, text="Yellow", variable=room, value=3).pack(side = "left")
Radiobutton(root, text="Orange", variable=room, value=4).pack(side = "left")

Radiobutton(root, text="Fireworks", variable=v, value=1).pack(side = "right")
Radiobutton(root, text="Fortnite", variable=v, value=2).pack(side = "right")
Radiobutton(root, text="Harry Potter", variable=v, value=3).pack(side = "right")
Radiobutton(root, text="Pokemon", variable=v, value=4).pack(side = "bottom")
Radiobutton(root, text="Minecraft", variable=v, value=5).pack(side = "bottom")

happy = Entry(root, text="Happy Birthday")
happy.insert(END, 'Happy Birthday')

happy.pack()

e = Entry(root, width=15)
e.pack(ipady=8)

myButton = Button(root, text="Make A Party", command=lambda: clicked(room.get()))
myButton.pack(side=TOP)


root.mainloop()