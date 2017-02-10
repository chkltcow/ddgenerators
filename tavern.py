import random
import json
from NPC import NPC
import random


class Tavern:
    def __init__(self, style=None):
        with open('tavern.json', 'r') as f:
            self.generator = json.load(f)
        if style:
            self.style = style
        else:
            self.style = random.choice(list(self.generator['menu']))
        self.name = self.generatename()
        self.menu = self.generatemenu()

    def generatename(self):
        method = self.generator['names']['methods'][random.choice(list(self.generator['names']['methods']))]
        string = method['string']
        choice1 = method['choice1']
        choice2 = method['choice2']
        name = string.format(random.choice(self.generator['names'][choice1]),
                             random.choice(self.generator['names'][choice2]))
        return name

    def generatemenu(self):
        string = "{} {} with {}, {}, and a side of {} and {} to drink"
        method = random.choice(self.generator['menu'][self.style]['method'])
        meat = random.choice(self.generator['menu'][self.style]['meat'])
        side1 = random.choice(self.generator['menu'][self.style]['side1'])
        side2 = random.choice(self.generator['menu'][self.style]['side2'])
        side3 = random.choice(self.generator['menu'][self.style]['side3'])
        drink = random.choice(self.generator['menu'][self.style]['drink'])
        menu = string.format(method, meat, side1, side2, side3, drink)
        return menu
