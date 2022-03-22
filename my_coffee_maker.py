
from pprint import pprint
from load_recipes import GetDrinkData, GetDrinksDict, refillMachine

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
refillMachine(machineResources)

while True:
    if cuvinte == HELP:
        print("Here are all the possible commands:", commands)
        cuvinte = input("Enter a command: ")

    if cuvinte == EXIT:
        print("Have a good day!")
        quit()

    if cuvinte == LIST_COFFEES:
        print(list(GetDrinksDict("recipes")))
        cuvinte = input("Enter a command: ")

    if cuvinte == REFILL:
        refillMachine(machineResources)
        print("The coffee machine was magically refilled!", machineResources)
        cuvinte = input("Enter a command: ")

    if cuvinte == RESOURCE_STATUS:
        print("Current resources:", machineResources)
        cuvinte = input("Enter a command: ")

    if cuvinte == MAKE_COFFEE:
        drinkName = input("Please enter the name of your desired drink: ")
        drinkDict = GetDrinksDict("recipes")
        recipe = drinkDict.get(drinkName)
        
        # Rezolva asta maine:
        # try:
        #     recipe = drinkDict.get(drinkName)
        # except:
        #     drinkName = input("We don't have this drink, please enter a new one: ")

        # recipe = GetDrinksDict("recipes").get(input("Please enter the name of your desired drink: "))     #Codul de mai sus int-o linie
        # print("Current resources:", machineResources)
        # print("Cost of your drink:", recipe)

        if int(machineResources.get("water")) >= int(recipe.get("water")) and int(machineResources.get("coffee")) >= int(recipe.get("coffee")) and int(machineResources.get("milk")) >= int(recipe.get("milk")): 
            machineResources["water"] = int(machineResources.get("water") - recipe.get("water"))
            machineResources["coffee"] = int(machineResources.get("coffee") - recipe.get("coffee"))
            machineResources["milk"] = int(machineResources.get("milk") - recipe.get("milk"))
            print(f"Here's your {drinkName}! Carefull, it's hot!")
            # print ("Remaining resources:", machineResources)
        else:
            print("Please refill the coffee machine!")
        cuvinte = input("Enter a command: ")
    
    else:
        cuvinte = input("This command is not recognized. Please enter a new command: ")



























