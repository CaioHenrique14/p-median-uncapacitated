import numpy as np
import csv

def readDatasets(filename, index):
    path = 'datasets\{filename}{index}.txt'.format(filename=filename, index=index)
    with open(path, 'r') as f:
        nrows, ncols = [int(field) for field in f.readline().split()]
        data = np.genfromtxt(f, dtype="int32", max_rows=nrows)
    return data

def readCsv(filename,index):
    with open('outputData\{filename}{index}.csv'.format(filename=filename,index=index), mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lineCount = 0
        sizeRow = 0
        for row in csv_reader:
            if lineCount == 0:
                 sizeRow = len(row)
            lineCount += 1
            print(row)
        print('\nMatriz {lineCount} por {sizeRow}.\n'.format(lineCount=lineCount,sizeRow=sizeRow))

def readAllFiles():
    for index in range(1, 6):
        readCsv('data', index)

def readFileByIndex(index):
    readCsv('data', index)