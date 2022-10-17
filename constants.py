from pathlib import Path

# Get the location of the home directory
homeDir = str(Path.home())

pynanceHomeDirName = "pynancedata"
pynanceHomeDir = homeDir + '/' + pynanceHomeDirName

# Header printed with every new CSV transaction file
csvTransactionHeader = "value;description;category;subcategory;timestamp"

def getCSVHeaders() -> list:
    return csvTransactionHeader.split(";")