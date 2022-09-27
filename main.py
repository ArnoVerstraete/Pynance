import pynance

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
        elif commandFirst == "exit":
            exit()

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
