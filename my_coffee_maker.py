
from pprint import pprint
from types import NoneType
from load_recipes import GetDrinksDict, refillMachine, resourceCondition

print("Hi! I'm the best coffee maker eva!!! Enter a command and i will fulfill it.")
print("To see a list of commands, please type 'help'")
cuvinte = input("Enter a command: ")

# Commands
HELP = "help"
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  
REFILL = "refill"
RESOURCE_STATUS = "status"
commands = [HELP, EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS]

machineResources = {}
refillMachine("all")
drinkDict = GetDrinksDict("recipes")

while True:
    if cuvinte == HELP:
        print("Here are all the possible commands:", commands)

    elif cuvinte == EXIT:
        print("Have a good day!")
        quit()

    elif cuvinte == LIST_COFFEES:
        print(list(drinkDict))

    elif cuvinte == REFILL:
        
        containerToRefill = input("Enter which container you want to refill: ")
        refillMachine(containerToRefill)
        print("The coffee machine was magically refilled!", machineResources)

    elif cuvinte == RESOURCE_STATUS:
        print("Current resources:", machineResources)

    elif cuvinte == MAKE_COFFEE:
        drinkName = input("Please enter the name of your desired drink: ")
        recipe = drinkDict.get(drinkName)

        if type(recipe) is NoneType:
            print("This drink is not available")
            
        
        #verifica daca nu e none

        # Rezolva asta maine:
        # try:
        #     recipe = drinkDict.get(drinkName)
        # except:
        #     drinkName = input("We don't have this drink, please enter a new one: ")

        if  resourceCondition(machineResources, recipe):
            machineResources["water"] = int(machineResources.get("water") - recipe.get("water"))
            machineResources["coffee"] = int(machineResources.get("coffee") - recipe.get("coffee"))
            machineResources["milk"] = int(machineResources.get("milk") - recipe.get("milk"))
            print(f"Here's your {drinkName}! Carefull, it's hot!")
        else:
            print("Please refill the coffee machine!")
    else:
        print("This command is not recognized.")
    cuvinte = input("Enter a command: ")



























