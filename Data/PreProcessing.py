import pandas as pd
# import numpy as np
import csv


def convertToCSV(fileName):
    rawFile = fileName
    rawFilePath = 'Data/RawData/'+rawFile
    rawName = (rawFile.split("."))[0]
    csvName = "Data/csvData/" + rawName + '.csv'
    dataFrame = pd.read_excel(rawFilePath)
    dataFrame.to_csv(csvName, index = False, header=True)


def fetchData(fileName):
    fileName = "Data/csvData/"+fileName
    fileName = (fileName.split("."))[0] + ".csv"
    results = []
    with open(fileName) as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            results.append(row)

    results.remove(results[0])
    for entry in results:
        time = entry[0]
        time = time.split(":")
        hour = time[0]
        minute = time[1]
        second = time[2]
        entry.remove(entry[0])
        entry.append(hour)
        entry.append(minute)
        entry.append(second)

    returnArray = []
    for entry in results:
        newEntry = []
        for value in entry:
            newEntry.append(float(value))
        returnArray.append(newEntry)
    return returnArray

def getBounds(fileName):
    fileName = "Data/csvData/"+fileName
    fileName = (fileName.split("."))[0] + ".csv"
    results = []
    with open(fileName) as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            results.append(row)

    min = None
    max = None
    returnArray = [min,max]

    results.remove(results[0])
    for entries in results:
        for item in entry: