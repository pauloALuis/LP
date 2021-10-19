"""
pd4.py
24/08/2021
"""

#4.a)
class Browser:
    """
    This class represents one web browsers with name and version as attributes
    """
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __str__(self):
        return "Nome do browser: " + self.name + " - Versão do browser: " + self.version

#4.b)
print(Browser.__doc__)

#4.c)
class ListaBrowsers(list):
    def __init__(self, browser : Browser):
        self.append(browser)

    def print_browsers(self):
        for el in self:
            print(el)

#4.d)
list_browser = ListaBrowsers(Browser("Opera", "2.2"))
list_browser.append(Browser("Chrome", "3.3"))
list_browser.append(Browser("M. Edge", "4.4"))
list_browser.append(Browser("I. Explorer", "9.2.1"))
list_browser.append(Browser("Mozilla", "1.2"))
#list_browser.print_browsers()

print(Browser.__bases__)