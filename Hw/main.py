from DataBase import Database
from Notebook import Notebook
from UserFilter import UserFilter


data = Database()
for i in range(0,10):
    data.addNew(data.createRandom())

filter = UserFilter(data.base)
filter.printBase()
while filter.userHere:
    filter.askFilter()
