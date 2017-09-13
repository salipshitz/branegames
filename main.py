from tkinter import *

class WindowMain(Frame):
    

	def __init__(self, master=None):
        self.pos = [lambda x: x*30+100 for x in range(10)]
		Frame.__init__(self, master)
		self.master = master
		self.master.title("Brane Games")
		self.pack(fill=BOTH, expand=1)
        self.start_screen()

	def start_screen(self):
		self.new_screen()
        
        self.showText("Hello everybody. Welcome to Brane Games")

        btn1 = Button(self, text="Continue", command=self.page_1)
        btn1.place(relx=0.5, y=35, anchor=CENTER)

    def showText(self, txt):
        text = Label(self, text=txt)
        text.pack()
		return text
	
	def showBtn(self, txt, command, x, y):
		btn = Button(self, text=txt, command=command)
		if x == True:
			btn.place(relx=0.5, y=y, anchor=True)
		else:
			btn.place(x=x, y=y)
		return btn

    def quitBtn(self):
		return self.showBtn("Quit", self.quit_app, 0, 0)

    def quit_app(self):
        exit()

    def new_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.quitBtn()

	def page_1(self):
        #Clear screen
       	self.new_screen()
       	#Text
       	self.showText("Two trains are heading at eachother.")
       	self.showText("Train A is traveling 50 miles per hour while Train B is traveling 50 kilometers per hour.")
       	self.showText("Assuming there's no wind and both trains left the station at the same time,")
       	self.showText("what is most likely to be yelled by the passengers on train A?")
		#Buttons
		self.showBtn("A: All of the above", None, True, pos[0])
		self.showBtn("B: Help!", None, True, pos[1])
		self.showBtn("C: Noooo!", None, True, pos[2])
		self.showBtn("D: Look out!", None, True, pos[3])
	
	def correct_1(self):
        self.new_screen()
		self.showText("Congratulations. The correct answers were: ")
        self.showBtn("F: 2 TRAINZ!!!", None, True, pos[0])
        self.showBtn("G: This needs to stop because if it doesn't ...", None, True, pos[1])
        self.showBtn("F: This is so stupid", None True, pos[2])
        self.showBtn("E: Who cares!", None, True, pos[3])
        self.showBtn("Continue 2 next page", self.page_2, True, pos[8])
        
    def incorrect_1(self):
        self.new_screen()
		self.showText("The answer is a. You have to thing outside the box. The correct answers were: ")
        self.showBtn("F: 2 TRAINZ!!!", None, True, pos[0])
        self.showBtn("G: This needs to stop because if it doesn't ...", None, True, pos[1])
        self.showBtn("F: This is so stupid", None True, pos[2])
        self.showBtn("E: Who cares!", None, True, pos[3])
        self.showBtn("Restart", self.start_screen, True, pos[4])
        self.showBtn("Quit", self.quit_app, True, pos[5])
    
    def page_2(self):
        self.showText("What do you see on the screen?")
        self.showText("A").config(font=("Arial", 30))
        self.showBtn("The letter A", None, True, pos[0])
        self.showBtn("The color black", None, True, pos[1])
        self.showBtn("The letter A, colored black", None, True, pos[2])
        self.showBtn("A ninety degree rotated unfinnished drawing of Pac-Man eating a Tic-Tac", None, True, pos[3])
        self.showBtn("A super zoomed in picture of the letter B", None, True, pos[4])
        
	
#Mainloop
root = Tk()
root.geometry("600x300")
app = WindowMain(root)
root.mainloop()
