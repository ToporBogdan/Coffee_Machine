# text de introducere
# optiune sa vezi ce comenzi stie aparatul

from pprint import pprint
import sys
import os

print("Hi! I'm the best coffee maker eva!!! Enter a command and i will fulfill it.")
print("To see a list of commands, please type 'help'")
# cuvinte = input("Enter a command: ")

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
commands = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

def GetDrinkData(drinkPath):
    drinkFile = open(drinkPath, "r")
    drinkLines = drinkFile.readlines()
    
    for i in range(len(drinkLines)):
        drinkLines[i] = drinkLines[i].strip("\n")
    # print(drinkLines)
    
    for i in range(len(drinkLines)):
        if i == 0:
            drinkLines[i] = [drinkLines[i]]
        else:
            drinkLines[i] = drinkLines[i].split("=")
    # print(drinkLines)
    drinkDict = {}
    drinkName = drinkLines[0][0]
    
    for i in range(1, len(drinkLines)):
        ingredientName = drinkLines[i][0]
        ingredientValue = int(drinkLines[i][1])
        drinkDict[ingredientName] = ingredientValue
    
    return (drinkName, drinkDict)


def GetDrinksDict(folderPath):
    drinks = {}
    all_files = os.listdir(folderPath)
    for file in all_files:
        currentDrink = GetDrinkData(folderPath + "/" + file)
        drinks[currentDrink[0]] = currentDrink[1]
    return drinks

pprint(GetDrinksDict("recipes"))








