from tkinter import *

class WindowMain(Frame):
    
	def __init__(self, master=None, name=""):
		Frame.__init__(self, master)
		self.master = master
		self.master.title("Brane Games")
        self.name = name
		self.pack(fill=BOTH, expand=1)
        self.start_screen()

	def start_screen(self):
		self.new_screen(None)
        
        self.showText("Hello everybody. Welcome to Brane Games")

        btn1 = Button(self, text="Continue", command=self.page_1)
        btn1.place(relx=0.5, y=35, anchor=CENTER)

    def showText(self, txt):
        t = Label(self, text=txt)
        t.pack()
		return t
	
	def showBtn(self, txt, command, x, y):
		b = Button(self, text=txt, command=command)
		if x == True:
			b.pack()
		else:
			b.place(x=x, y=y)
		return b
    
    def showIncBtn(self, txt):
        showBtn(txt, self.cur_incorrect, True, None)

    def quitBtn(self):
		return self.showBtn("Quit", self.quit_app, 0, 0)

    def quit_app(self):
        exit()

    def new_screen(self, inc_func):
        for widget in self.winfo_children():
            widget.destroy()
        self.quitBtn()
        self.cur_incorrect = inc_func

	def page_1(self):
        #Clear screen
       	self.new_screen(self.incorrect_1)
       	#Text
       	self.showText("Two trains are heading at eachother.")
       	self.showText("Train A is traveling 50 miles per hour while Train B is traveling 50 kilometers per hour.")
       	self.showText("Assuming there's no wind and both trains left the station at the same time,")
       	self.showText("what is most likely to be yelled by the passengers on train A?")
		#Buttons
		self.showBtn("A: All of the above", correct_1, True, None)
		self.showIncBtn("B: Help!")
		self.showIncBtn("C: Noooo!")
		self.showIncBtn("D: Look out!")
	
	def correct_1(self):
        self.new_screen(None)
		self.showText("Congratulations. Can you beat level 2 TRAINZ!!!?")
        self.showBtn("F: 2 TRAINZ!!!", None, True, None)
        self.showBtn("G: This needs to stop because if it doesn't ...", None, True, None)
        self.showBtn("F: This is so stupid", None True, None)
        self.showBtn("E: Who cares!", None, True, None)
        self.showBtn("Continue 2 next page", self.page_2, True, None)
        
    def incorrect_1(self):
        self.new_screen()
		self.showText("The answer is A. You have to thing outside the box. The correct answers were: ")
        self.showBtn("F: 2 TRAINZ!!!", None, True, None)
        self.showBtn("G: This needs to stop because if it doesn't ...", None, True, None)
        self.showBtn("F: This is so stupid", None True, None)
        self.showBtn("E: Who cares!", None, True, None)
        self.showBtn("Restart", self.start_screen, True, None)
        self.showBtn("Quit", self.quit_app, True, None)
    
    def page_2(self):
        self.showText("What do you see on the screen?")
        self.showText("A").config(font=("Arial", 30))
        self.showBtn("The letter A", None, True, None)
        self.showBtn("The color black", None, True, None)
        self.showBtn("The letter A, colored black", None, True, None)
        self.showBtn("A ninety-degree rotated unfinished drawing of Pac-Man eating a Tic-Tac", self.correct_2, True, None)
        self.showBtn("A super zoomed in picture of the letter B", None, True, None)
        
    def correct_2(self):
        self.showText("Congrats. You have passed.")
        self.showBtn("Restart", self.start_screen, True, None)
        self.showBtn("Quit", self.quit_app, True, None)
        
    def incorrect_2(self):
        self.showText(self.name + ", you are absolutely wrong.")
        self.showText("The correct answer is:")
        self.showBtn("A ninety-degree rotated unfinished drawing of Pac-Man eating a Tic-Tac", None, True, None)
        
#Mainloop
name = input("Enter your name:\n")
root = Tk()
root.geometry("600x300")
app = WindowMain(root, name)
root.mainloop()
