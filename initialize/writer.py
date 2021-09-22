import numpy as np

def writeResult(result,index):
    resultFormatted = np.asarray(result)
    np.savetxt('outputData/data{index}.csv'.format(index=index), resultFormatted, fmt='%.4f', delimiter=',')