# Cleaner filters and modifies raw data from bs4

import bs4

class Cleaner:
    def __init__(self, elems):
        self.elems = elems


    # gets the text in the elements retrieved from bs4
    def getText(self):
        elems = self.elems

        newElemList = []
        for elem in elems:
            temp = []
            for words in elem:
                temp.append(words.getText())
            newElemList.append(temp)

        self.elems = newElemList


    # adds index to each element in input list
    def addIndex(self, listIndex):
        elems = self.elems

        temp = []
        for index, words in enumerate(elems[listIndex]):
            indexAdded = f"{index + 1}. {words}"
            temp.append(indexAdded)

        self.elems[listIndex] = temp



