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
        btnA = self.showBtn("A: All of the above", self.correct_1, True, 100)
	    btnB = self.showBtn("B: Help!", None, True, 130)
        btnC = self.showBtn("C: Noooo!", None, True, 160)
	    btnD = self.showBtn("D: Look out!", None, True, 190)
        
    def correct_1(self):
        self.killWidgets()
        self.showText("Congrats! You got it correct")
        self.showBtn("Continue", self.page_2, True, 50)
        self.showBtn("Quit", self.quit_app, True, 80)
        self.showBtn("Restart", self.start_screen, True, 110)
    
    def incorrect_1(self):
        self.killWidgets()
        self.showText("The answers B, C, and D would've been right if we were talking about train B,")
        self.showText("as it's probably full of foreigners seeing as they measure in kilometers.")
        self.showText("But, we're talking about train A which is probably full of Americans.")
        self.showText("You have to think outside the box. The correct answers we were looking for are:")
        self.showBtn("E: Who cares?", None, True, 100)
        self.showBtn("F: This is so dumb.", None, True, 130)
        self.showBtn("G: This needs to stop because if it doesn't ...", None, True, 160)
        self.showBtn("H: 2 TRAINZ!!!", None, True, 190)
        self.showBtn("Restart", self.start_screen, True, 280)
        self.showBtn("Quit", self.quit_app, True, 310)
        
    def page_2(self):
        self.killWidgets()
        self.showText("Under contruction")
        
#Mainloop
root = Tk()
root.geometry("800x400")
app = WindowMain(root)
root.mainloop()
