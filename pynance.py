'''
Handles transactions and stores
'''

import constants

import pathlib
import logging
from glob import glob

def newFinance(filename, directory=None) -> str:
    '''
    Create new finance store
    Returns path to store
    '''
    storeLocation = ""

    if directory != None:
        storeLocation = directory
    else:
        storeLocation = constants.pynanceHomeDir
        makeHomeDir()

    fullpath = storeLocation + "/" + filename + ".csv"
    
    logging.info("Creating new finance store: " + fullpath)
    with open(fullpath, "w+") as f:
        f.writelines(constants.csvTransactionHeader)

    return fullpath

def makeHomeDir() -> None:
    '''
    Checks if the data directory for pynance already exists in the user's home directory
    '''
    pathlib.Path(constants.pynanceHomeDir).mkdir(parents=True, exist_ok=True)

def checkFinanceStoresInHomeDir() -> list:
    '''
    Returns array of found finance stores in the home directory
    '''
    return glob(constants.pynanceHomeDir + "/*" + ".csv")

def getFinanceName(path) -> str:
    '''
    Returns only the filename of the given path
    '''
    s = path.split('/')
    return s[-1]

def getBalance(storePath) -> float:
    '''
    Checks the account balance of the given finance store
    '''
    
    balance = 0

    with open(storePath) as f:
        isFirstline = True
        for line in f:
            if isFirstline:
                isFirstline = False
                continue
            d = readTransaction(line)
            balance += float(d["value"])
    
    return balance

def readTransaction(transactionString) -> dict:
    '''
    Returns the values of the transaction into a dictionary
    '''
    headers = constants.getCSVHeaders()
    values = transactionString.split(',')
    d = dict()
    for keyindex in range(0, len(headers)):
        d[headers[keyindex]] = values[keyindex]

    return d 

def addTransaction(value, description, category, subcategory, timestamp, store) -> bool:
    '''
    Adds the new transaction to the given account. Returns value indicates success. 
    '''

    logging.info("Adding new transaction: ", value, description, category, subcategory, timestamp, store)

    with open(store, 'w') as f:
        f.writelines(value + ',' + description + ',' + category + ',' + subcategory + ',' + str(timestamp))
    return True