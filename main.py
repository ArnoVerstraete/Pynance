import pynance
import categories
from datetime import datetime

pynance.makeHomeDir()

existingStores = pynance.checkFinanceStoresInHomeDir()
currFinanceStore = ""

def loopCommands() -> None:
    while(True):
        command = input()

        commandSplit = command.split(" ")
        commandFirst = commandSplit[0]

        if commandFirst == "h" or commandFirst == "help":
            print("Help...")
        elif commandFirst == "l" or commandFirst == "list":
            print("List transactions...")
        elif commandFirst == "b" or commandFirst == "balance":
            print(pynance.getBalance(currFinanceStore))
        elif commandFirst == "a" or commandFirst == "add":
            handleAdd(command, commandSplit, commandFirst)
        elif commandFirst == "exit":
            exit()

def handleAdd(command, commandSplit, commandFirst) -> None:
    value = ""
    description = ""
    category = ""
    subcategory = ""
    timestamp = datetime.timestamp(datetime.now())

    if len(command) == 1:
        value = input("Value: ")
        description = input("Description: ")
        category = input("Category: ").lower()
        subcategory = input("Subcategory (leave empty for no subcategory): ").lower()

    elif len(command) == 5 or len(command) == 4:
        value = commandSplit[1]
        description = commandSplit[2]
        category = commandSplit[3].lower()

        if len(command) == 5:
            subcategory = commandSplit[4].lower()
        else:
            subcategory = category

    print(
        "Value: ", value,
        "\nDescription: ", description,
        "\nCategory: ", category,
        "\nSubcategory: ", subcategory,
        "\nTimestamp: ", datetime.utcfromtimestamp(timestamp).strftime('%d-%m-%Y %H:%M:%S')
    )

    while True:
        inp = input("Add transaction? (Y/n)")
        if inp == "" or inp.lower() == "y":
            pynance.addTransaction(value, description, category, subcategory, timestamp, currFinanceStore)
            return
        elif inp.lower() == "n":
            break

while True:
    if currFinanceStore != "":
        loopCommands()
    elif len(existingStores) != 0:
        print("Available finance stores:")
        print(existingStores)
        i = input("Store index: ")
        currFinanceStore = existingStores[int(i)]
    else:
        newStoreName = input("Create new finance store: ")
        currFinanceStore = pynance.newFinance(newStoreName)
