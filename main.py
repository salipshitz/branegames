from tkinter import *

class WindowMain(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Brane Games")
        self.pack(fill=BOTH, expand=1)

        self.quitBtn()
        
        self.showText("Hello everybody. Welcome to Brane Games")

        twoButton = Button(self, text="Continue", command=self.page_2)
        twoButton.place(relx=0.5, y=35, anchor=CENTER)

    def showText(self, txt):
        text = Label(self, text=txt)
        text.pack()

    def quitBtn(self):
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()

    def killWidgets(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.quitBtn()

    def page_2(self):
        #Clear screen
        self.killWidgets()
        #Text
        self.showText("Two trains are heading at eachother.")
        self.showText("Train A is traveling 50 miles per hour while Train B is traveling 50 kilometers per hour.")
        self.showText("Assuming there's no wind and both trains left the station at the same time,")
        self.showText("what is most likely to be yelled by the passengers on train A?")
        #Buttons
        btnA = Button(self, text="A: All of the above", command=None)
        btnA.place(relx=0.5, y=100, anchor=CENTER)

        btnB = Button(self, text="B: Help!", command=None)
        btnB.place(relx=0.5, y=130, anchor=CENTER)

        btnC = Button(self, text="C: Noooo!", command=None)
        btnC.place(relx=0.5, y=160, anchor=CENTER)

        btnD = Button(self, text="
#Mainloop
root = Tk()
root.geometry("600x300")
app = WindowMain(root)
root.mainloop()
