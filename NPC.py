import random
import ddutils
from elizabeth import Personal
import json


class NPC:
    def __init__(self, race=None, gender=None):
        # Open and parse JSON tables
        with open('DMGtables.json', 'r') as f:
            tables = json.load(f)
        with open('races.json', 'r') as f:
            races = json.load(f)

        # Random gender and race if not assigned
        if gender:
            self.gender = gender
        else:
            self.gender = random.choice(['male', 'female'])
        if race:
            self.race = race
        else:
            self.race = random.choice(['human', 'dwarf', 'elf', 'gnome', 'halfelf', 'halfling'])

        # Initialize name creation via Elizabeth
        locale = random.choice(races[self.race]['locale'])
        user = Personal(locale)

        # Basics
        self.name = user.full_name(gender=self.gender)
        self.racename = races[self.race]['racename']
        minage = races[self.race]['age']['adulthood']
        maxage = races[self.race]['age']['old'] + ddutils.roll(races[self.race]['age']['maxage'])
        middleage = races[self.race]['age']['middleage']
        self.age = round(random.triangular(minage, maxage, middleage))
        baseheight = races[self.race]['size'][self.gender]['baseheight']
        baseweight = races[self.race]['size'][self.gender]['baseweight']
        sizemod = races[self.race]['size'][self.gender]['sizemod']
        weightmod = races[self.race]['size'][self.gender]['weightmod']
        self.height = baseheight + ddutils.roll(sizemod)
        self.weight = baseweight + (ddutils.roll(sizemod) * weightmod)
        
        # Kludge to describe how old an NPC is
        if self.age > int(races[self.race]['age']['venerable']) + ((maxage-races[self.race]['age']['venerable'])/2):
            self.agedesc = 'elderly'
        elif self.age > int(races[self.race]['age']['venerable']):
            self.agedesc = 'venerable'
        elif self.age > int(races[self.race]['age']['old']):
            self.agedesc = 'aging'
        elif self.age > int(races[self.race]['age']['middleage']):
            self.agedesc = 'middle age'
        else:
            self.agedesc = 'young'

        # Attributes
        self.appearance = random.choice(tables['appearance'])
        self.highability = random.choice(tables['abilities']['high'])
        self.lowability = random.choice(tables['abilities']['low'])
        while self.lowability['roll'] == self.highability['roll']:
            self.lowability = random.choice(tables['abilities']['low'])
        self.talent = random.choice(tables['talent'])
        self.mannerism = random.choice(tables['mannerisms'])
        self.interaction = random.choice(tables['interaction'])
        self.alignment = random.choice(tables['ideals']['ideal'])
        self.ideal = random.choice(tables['ideals'][self.alignment])
        self.bonds = []
        bond = random.choice(tables['bond'])
        if bond['roll'] == '10':
            while len(self.bonds) < 2:
                bond = random.choice(tables['bond'])
                if bond not in self.bonds and bond['roll'] != '10':
                    self.bonds.append(bond)
        else:
            self.bonds.append(bond)
        self.flaw = random.choice(tables['flaw'])

    def printdescription(self):
        print(self.name)
        print("{} {} {}".format(self.agedesc.title(), self.gender.title(), self.racename))
        print("{} years old".format(round(self.age)))
        print("{} tall, {} lbs".format(ddutils.height_in_feet(self.height), round(self.weight)))
        print("Appearance: {}".format(self.appearance['desc']))
        print("High Stat: {}".format(self.highability['desc']))
        print("Low Stat:  {}".format(self.lowability['desc']))
        print("Talent: {}".format(self.talent['desc']))
        print("Mannerism: {}".format(self.mannerism['desc']))
        print("Interaction: {}".format(self.interaction['desc']))
        print("{} ideal:  {}".format(self.alignment.title(), self.ideal['desc']))
        for bond in self.bonds:
            print("Bond: {}".format(bond['desc']))
        print("Flaw: {}".format(self.flaw['desc']))

    def description(self):
        description = ""
        description += self.name + "\n"
        description += "{} {} {}\n".format(self.agedesc.title(), self.gender.title(), self.racename)
        description += "{} years old\n".format(round(self.age))
        description += "{} tall, {} lbs\n".format(ddutils.height_in_feet(self.height), round(self.weight))
        description += "Appearance: {}\n".format(self.appearance['desc'])
        description += "High Stat: {}\n".format(self.highability['desc'])
        description += "Low Stat:  {}\n".format(self.lowability['desc'])
        description += "Talent: {}\n".format(self.talent['desc'])
        description += "Mannerism: {}\n".format(self.mannerism['desc'])
        description += "Interaction: {}\n".format(self.interaction['desc'])
        description += "{} ideal:  {}\n".format(self.alignment.title(), self.ideal['desc'])
        for bond in self.bonds:
            description += "Bond: {}\n".format(bond['desc'])
        description += "Flaw: {}\n".format(self.flaw['desc'])
        return description

    def json(self):
        """
        Returns JSON dump of character
        """
        return json.dumps(self.__dict__)