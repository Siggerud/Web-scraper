import requests, bs4

class Parser:
    def __init__(self, URL, selectors):
        res = requests.get(URL)
        res.raise_for_status()
        self.url = res.url

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        self.elems = self.getElems(soup, selectors)



    def getElems(self, soup, selectors):
        elems = []
        for selector in selectors:
            elems.append(soup.select(selector))

        return elems











