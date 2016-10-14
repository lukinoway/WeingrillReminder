########################################
# - Title:   Weingrill Menu Parser/Importer
# - Author:  Lukas Pichler
# - Date:    2016-10-12
########################################

class Menu:
    def __init__(self):
        self.day_list = []
        self.food_list = []

    def addDay(self, date):
        self.day_list.append(date)

    def addFood(self, food):
        self.food_list.append(food)

class Food:

    def __init__(self, starter, main, dessert):
        self.starter = starter
        self.main = main
        self.dessert = dessert

    def printer(self):
        print(("starter: \t%s" % self.starter))
        print(("main:    \t%s" % self.main))
        print(("dessert: \t%s" % self.dessert))

import db_connector
import urllib
from bs4 import BeautifulSoup

# main link to get menu
link = "http://www.weingrill.info/content/menuplan.php"

print(("get data from: " + link))

# load content
soup = BeautifulSoup(urllib.urlopen(link), 'html.parser')
content = soup.dl

menu = Menu()

# get date info
for day in content.find_all('dt'):
    datestr = day.get_text().split(',')
    menu.addDay(datestr[1].strip())

#get food info
for food in content.find_all('dd'):
    main = food.strong.get_text().strip()
    dessert = food.br.br.get_text().strip()

    # simplify string
    food.br.decompose()
    starter = food.get_text().strip()

    # add to list
    x = Food(starter, main, dessert)
    menu.addFood(x)

# import part
print "\nTime to import data"
db_connector.connect()
for i in range(len(menu.day_list)):
    print(("\n%s" % menu.day_list[i]))
    print("Menu: ")
    menu.food_list[i].printer()
    db_connector.import_data(menu.day_list[i], menu.food_list[i].starter, menu.food_list[i].main, menu.food_list[i].dessert)

# close connection
db_connector.close()