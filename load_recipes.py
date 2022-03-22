"""
	Bonus task: load all the available coffee recipes from the folder 'recipes/'
	File format:
		first line: coffee name
		next lines: resource=percentage

	info and examples for handling files:
		http://cs.curs.pub.ro/wiki/asc/asc:lab1:index#operatii_cu_fisiere
		https://docs.python.org/3/library/io.html
		https://docs.python.org/3/library/os.path.html
"""
import os
from pprint import pprint

RECIPES_FOLDER = "recipes"


def GetDrinkData(drinkPath):
	drinkFile = open(drinkPath, "r")
	drinkLines = drinkFile.readlines()
	for i in range(len(drinkLines)):
		drinkLines[i] = drinkLines[i].strip("\n")
	# print(drinkLines)										#aici avem o singura lista pt fiecare bautura

	for i in range(len(drinkLines)):
		if i == 0:
			drinkLines[i] = [drinkLines[i]]
		else:
			drinkLines[i] = drinkLines[i].split("=")
	# print(drinkLines)										#aici avem o lista de liste pt fiecare bautura
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

def refillMachine(machineResources):
	machineResources["water"] = 100
	machineResources["coffee"] = 100
	machineResources["milk"] = 100

"""
toate functiile sa le mut aici si le import in partea cealalta
"""