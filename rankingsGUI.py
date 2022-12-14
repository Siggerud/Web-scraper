# rankingsGUI creates a GUI that shows the current top 10 in my favorite three sports

from tkinter import *
from tkinter import ttk
from webScraper import Parser
from Cleaner import Cleaner
import webbrowser

# create layout of GUI
class rankingsGUI:
    def __init__(self, master):
        self.master = master
        master.geometry("450x400")
        master.title("Top 10 leaderboards")

        self.Tabs = ttk.Notebook(master)
        self.formula1 = ttk.Frame(self.Tabs, width=450, height=400)
        self.mma = ttk.Frame(self.Tabs, width=450, height=400)
        self.boxing = ttk.Frame(self.Tabs, width=450, height=400)

        self.Tabs.add(self.formula1, text="Formula 1")
        self.Tabs.add(self.mma, text="MMA")
        self.Tabs.add(self.boxing, text="Boxing")

        self.Tabs.grid(row=0, column=0)

        self.getFormula1LeaderBoards()
        self.getMMArankings()
        self.getBoxingP4P()


    # create layout for boxing tab
    def getBoxingP4P(self):
        URL = "https://www.ringtv.com/ratings/"
        parser = Parser(URL=URL, selectors=['div[class="name"]'])
        elems = parser.elems

        cleaner = Cleaner(elems)
        cleaner.getText()
        cleaner.addIndex(0)

        boxingNames = cleaner.elems[0]

        for index, name in enumerate(boxingNames):
            boxingLabel = Label(self.boxing, text=name, font="Arial")
            boxingLabel.grid(row=index, column=0, sticky="w", pady=1)

        LinkBoxingButton = Button(self.boxing, text="Source link", command= lambda: self.openLink(URL), fg="blue")
        LinkBoxingButton.grid(column=1)


    # opens link to the source for rankings
    def openLink(self, URL):
        webbrowser.open(URL)


    # creates layout for mma tab
    def getMMArankings(self):
        URL = "https://www.tapology.com/rankings/current-top-ten-best-pound-for-pound-mma-and-ufc-fighters"
        parser = Parser(URL=URL, selectors=['h1 a'])
        elems = parser.elems

        cleaner = Cleaner(elems)
        cleaner.getText()
        cleaner.addIndex(0)

        mmaFighterNames = cleaner.elems[0][:10]

        for index, name in enumerate(mmaFighterNames):
            mmaLabel = Label(self.mma, text=name, font="Arial")
            mmaLabel.grid(row=index, column=0, sticky="w", pady=1)

        LinkMMAButton = Button(self.mma, text="Source link", command=lambda: self.openLink(URL), fg="blue")
        LinkMMAButton.grid(column=1)


    # creates layout for formula 1 leaderboards
    def getFormula1LeaderBoards(self):
        URL = "https://www.formula1.com/en/results.html/2022/drivers.html"
        parser = Parser(URL=URL, selectors = ['span[class="hide-for-tablet"]', 'span[class="hide-for-mobile"]'])
        elems = parser.elems

        cleaner = Cleaner(elems)
        cleaner.getText()
        cleaner.addIndex(0)

        driverNames = []
        for i in range(10): # the full names had to comprised of two lists
            driverNames.append(cleaner.elems[0][i] + " " + cleaner.elems[1][i])

        for index, driverName in enumerate(driverNames):
            driverLabel = Label(self.formula1, text=f"{driverName}", font="Arial")
            driverLabel.grid(row=index, column=0, sticky="w", pady=1)

        LinkF1Button = Button(self.formula1, text="Source link", command=lambda: self.openLink(URL), fg="blue")
        LinkF1Button.grid(column=1)


root = Tk()
rankingsGUI = rankingsGUI(root)
root.mainloop()