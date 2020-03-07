from Data.PreProcessing import convertToCSV
from Data.PreProcessing import fetchData

fileName = "mar6.csv"
# convertToCSV(fileName)
data = fetchData(fileName)
print(data[0])