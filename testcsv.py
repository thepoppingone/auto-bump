import csv

with open('listingData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    firstRow = next(readCSV)
    secondRow = next(readCSV)
    title,price,category,desc = secondRow
    print(desc)
