'''
Handles category management
'''

import constants

import pathlib
import logging
from glob import glob

# Dictionary where the keys are the main categories and the values are arrays of subcategories
categories = {}
categoriesCached = False

def checkIfCategoryExists(category, storePath, isSubCategory) -> bool:
    '''
    Checks if the given category or subcategory has been used before
    '''

    global categoriesCached
    if not categoriesCached:
        cacheCategories(storePath)

    for k in categories.keys():
        for sk in categories[k]:
            if sk == category:
                return True
    
    return False

def newCategory(category) -> None:
    addCategoryToCache(category, category)

def newSubCategory(category, subcategory) -> None:
    addCategoryToCache(category, subcategory)

def cacheCategories(storePath) -> dict:
    '''
    Loops through the given store and gathers all categories and subcategories
    '''
    with open(storePath) as f:
        categoryIndex = None
        subCategoryIndex = None
        isFirstLine = True
        for line in f:
            if isFirstLine:
                isFirstLine = False
                split = line.split(';')
                for i in range(0,len(split)):
                    if split[i] == "category":
                        categoryIndex = i
                    elif split[i] == "subcategory":
                        subCategoryIndex = i

            else:
                currCategory = line[categoryIndex]
                currSubcategory = line[subCategoryIndex]

                addCategoryToCache(currCategory, currSubcategory)

    global categoriesCached
    categoriesCached = True
    return categories

def addCategoryToCache(category, subcategory) -> None:
    if category in categories.keys():
        # If category is the same as the subcategory the value is stored without subcategory
        if category != subcategory:
            # Add subcategory
            if subcategory not in categories[category]:
                categories[category].append(subcategory)
    else:
        # New category, check if we need to add a subcategory as well
        subactegories = []
        if category != subcategory:
            subactegories.append(subcategory)
        categories[category] = subactegories

    return