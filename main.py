import pynance
import categories
from datetime import datetime

pynance.makeHomeDir()

existingStores = pynance.checkFinanceStoresInHomeDir()
currFinanceStore = ""

def loopCommands() -> None:
    handleOverview()

    while(True):
        command = input()

        commandSplit = command.split(" ")
        commandFirst = commandSplit[0].lower()

        if commandFirst == "h" or commandFirst == "help":
            print("Help...")
        elif commandFirst == "l" or commandFirst == "list":
            handleList()
        elif commandFirst == "b" or commandFirst == "balance":
            print(pynance.getBalance(currFinanceStore))
        elif commandFirst == "mb" or commandFirst == "monthlybalance":
            print(pynance.getMonthlyBalance(currFinanceStore))
        elif commandFirst == "a" or commandFirst == "add":
            handleAdd(command, commandSplit, commandFirst)
        elif commandFirst == "o" or commandFirst == "overview":
            handleOverview()

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

def handleOverview() -> None:
    print(pynance.getBalance(currFinanceStore))

def handleList() -> None:
    for t in pynance.getTransactionsList(currFinanceStore):
        print(t.value, t.description. t.category, t.subcategory, datetime.utcfromtimestamp(t.date).strftime('%d-%m-%Y %H:%M:%S'))

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
