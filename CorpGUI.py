import Corp
import tkinter
from sys import platform
def createCharUI:

def gui_start():
	MainMenu = Tk()
	MainMenu.geometry('500x500+400+300')
	MainMenu.configure(background='black')
	if str(platform) is 'win32'
		MainMenu.mainloop()
	MainMenu.title('Main Menu')
	label1 = Label(MainMenu,text='Welcome to CorpHelper',font('Helvetica', 16)).pack()
	###
	buttonA = Button(MainMenu,text='Create a Character',command=createCharUI).place(x=75,y=10)
	buttonB	= Button(MainMenu,text='Lockpicking',command=LockpickUI).place(x=100,y=10)
