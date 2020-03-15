from Data.PreProcessing import convertToCSV
from Data.PreProcessing import fetchData
from Data.PreProcessing import fetchLabels

fileName = "mar9-data2 (small) PLX-DAQ.xlsx"
csvFileName = convertToCSV(fileName)
data = fetchData(csvFileName)

print(data[0])

year = int(2020)
month = int(3)
day = int(6)
latitude = int(48.463522)
longitude = int(-123.310644)
timezone = int(-8)
Labels = fetchLabels(data, year, month, day, latitude, longitude, timezone)
print(Labels[0])
