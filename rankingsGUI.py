from tkinter import *
from tkinter import ttk
from webScraper import Parser
from Cleaner import Cleaner

# TODO
# lag en tab for boksing

class rankingsGUI:
    def __init__(self, master):
        self.master = master
        master.geometry("400x550")
        master.title("Top 10 leaderboards")

        self.Tabs = ttk.Notebook(master)
        self.formula1 = ttk.Frame(self.Tabs, width=400, height=550)
        self.mma = ttk.Frame(self.Tabs, width=400, height=550)
        self.boxing = ttk.Frame(self.Tabs, width=400, height=550)

        self.Tabs.add(self.formula1, text="Formula 1")
        self.Tabs.add(self.mma, text="MMA")
        self.Tabs.add(self.boxing, text="Boxing")

        self.Tabs.grid(row=0, column=0)

        self.getFormula1LeaderBoards()
        self.getMMArankings()
        self.getBoxingP4P()


    def getBoxingP4P(self):
        parser = Parser(URL="https://www.ringtv.com/ratings/", selectors=['div[class="name"]'])
        elems = parser.elems

        cleaner = Cleaner(elems)
        cleaner.getText()
        cleaner.addIndex(0)

        boxingNames = cleaner.elems[0]

        for index, name in enumerate(boxingNames):
            boxingLabel = Label(self.boxing, text=name, font="Arial")
            boxingLabel.grid(row=index, column=0, sticky="w", pady=5)


    def getMMArankings(self):
        parser = Parser(URL="https://www.tapology.com/rankings/current-top-ten-best-pound-for-pound-mma-and-ufc-fighters", selectors=['h1 a'])
        elems = parser.elems

        cleaner = Cleaner(elems)
        cleaner.getText()
        cleaner.addIndex(0)

        mmaFighterNames = cleaner.elems[0][:10]

        for index, name in enumerate(mmaFighterNames):
            mmaLabel = Label(self.mma, text=name, font="Arial")
            mmaLabel.grid(row=index, column=0, sticky="w", pady=1)


    def getFormula1LeaderBoards(self):
        parser = Parser(URL="https://www.formula1.com/en/results.html/2022/drivers.html", selectors = ['span[class="hide-for-tablet"]', 'span[class="hide-for-mobile"]'])
        elems = parser.elems

        cleaner = Cleaner(elems)
        cleaner.getText()
        cleaner.addIndex(0)

        driverNames = []
        for i in range(10):
            driverNames.append(cleaner.elems[0][i] + " " + cleaner.elems[1][i])

        for index, driverName in enumerate(driverNames):
            driverLabel = Label(self.formula1, text=f"{driverName}", font="Arial")
            driverLabel.grid(row=index, column=0, sticky="w", pady=1)

root = Tk()
rankingsGUI = rankingsGUI(root)
root.mainloop()