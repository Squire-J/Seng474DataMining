import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from math import sin
from math import cos

def getScore(calculatedLabels, expectedLabels, tolerance):
    score = 0
    total = len(calculatedLabels)
    print("Tolerance: "+str(tolerance))
    for i in range (total):
        calculatedAlpha = calculatedLabels[i][0]
        calculatedBeta = calculatedLabels[i][1]
        expectedAlpha = expectedLabels[i][0]
        expectedBeta = expectedLabels[i][1]

        differenceAlpha = int(expectedAlpha * tolerance)
        differenceBeta = int(expectedBeta * tolerance)

        upperboundAlpha = expectedAlpha + differenceAlpha
        lowerboundAlpha = expectedAlpha - differenceAlpha
        upperboundBeta = expectedBeta + differenceBeta
        lowerboundBeta = expectedBeta - differenceBeta

        if (calculatedAlpha > upperboundAlpha) or (calculatedAlpha < lowerboundAlpha):
            continue
        elif (calculatedBeta > upperboundBeta) or (calculatedBeta < lowerboundBeta):
            continue

        score = score + 1
    print("Score: "+str(score/total)+"\n")
    return score/total

def processLabels(data):
    returnData = []
    elevation = 0
    azimuth = 1
    r = 1
    for entry in data:
        newEntry = []

        x = r * cos(elevation) * cos(azimuth)
        y = r * cos(elevation) * sin(azimuth)
        z = r * sin(elevation)
        
        newEntry.append(x)
        newEntry.append(y)
        newEntry.append(z)

        returnData.append(newEntry)
    return returnData


def plotTracing(simpleLabels, complicatedLabels, expectedLabels):
    fig = plt.figure()
    ax = Axes3D(fig)
    simple = np.asarray(processLabels(simpleLabels))
    complicated = np.asarray(processLabels(complicatedLabels))
    expected = np.asarray(processLabels(expectedLabels))

    print(expected)

    ax.scatter(expected[:,0], expected[:,1], expected[:,2], marker = 'x', color = 'k')
    # ax.scatter(simple[:,0], simple[:,1], simple[:,2], marker = 'o', color = 'r')
    # ax.scatter(complicated[:,0], complicated[:,1], complicated[:,2], marker = 'o', color = 'b')
    
    plt.show()