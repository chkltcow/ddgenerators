import random
import math


def inches_to_meters(inches):
    return float(inches) * 0.0254


def meters_to_inches(meters):
    return float(meters) / 0.0254


def inches_to_feet(inches):
    return float(inches) / 12.0


def feet_to_inches(feet):
    return float(feet) * 12.0


def calc_bmi(height, weight):
    return float(weight)/(float(height) * float(height))


def lbs_to_kg(lbs):
    return float(lbs) * 0.453592


def kg_to_lbs(kg):
    return float(kg) * 2.20462


def rollstat4d6():
    dice = []
    for i in range(4):
        dice.append(random.randint(1, 6))
    dice.sort(reverse=True)
    return sum(dice[:3])


def rollstat3d6():
    dice = []
    for i in range(3):
        dice.append(random.randint(1, 6))
    return sum(dice)


def roll(dice):
    total = 0
    plussplit = dice.split("+")
    if len(plussplit) > 1:
        bonus = int(plussplit[1])
    else:
        bonus = 0
    qty, value = plussplit[0].split("d")
    for i in range(int(qty)):
        die = random.randint(1, int(value)+1)
        total += die
    return total + bonus


def height_in_feet(inches):
    feet = math.floor(inches_to_feet(inches))
    return "{}'{}\"".format(feet, inches-(feet*12))


def statmod(stat):
    return math.floor((stat-10) / 2)