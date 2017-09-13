from tkinter import *

class WindowMain(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.start_screen()

    def start_screen(self):
        self.master.title("Brane Games")
        self.pack(fill=BOTH, expand=1)

        self.quitBtn()
        
        self.showText("Hello everybody. Welcome to Brane Games")

        oneBtn = Button(self, text="Continue", command=self.page_1)
        oneBtn.place(relx=0.5, y=35, anchor=CENTER)

    def showText(self, txt):
        text = Label(self, text=txt)
        text.pack()
	
	def showBtn(self, txt, command, x, y):
		btn = Button(self, text=txt, command=command)
		if x == True:
			btn.place(relx=0.5, y=y, anchor=True)
		else:
			btn.place(x=x, y=y)
		return btn

    def quitBtn(self):
		self.showBtn("Quit", self.quit_app, 0, 0)

    def quit_app(self):
        exit()

    def killWidgets(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.quitBtn()

    def page_1(self):
        #Clear screen
        self.killWidgets()
        #Text
        self.showText("Two trains are heading at eachother.")
        self.showText("Train A is traveling 50 miles per hour while Train B is traveling 50 kilometers per hour.")
        self.showText("Assuming there's no wind and both trains left the station at the same time,")
        self.showText("what is most likely to be yelled by the passengers on train A?")
        #Buttons
        btnA = self.showBtn("A: All of the above", None, True, 100)
		btnB = self.showBtn("B: Help!", None, True, 130)
		btnC = self.showBtn("C: Noooo!", None, True, 160)
		btnD = self.showBtn("D: :(", None, True, 190)
#Mainloop
root = Tk()
root.geometry("600x300")
app = WindowMain(root)
root.mainloop()
