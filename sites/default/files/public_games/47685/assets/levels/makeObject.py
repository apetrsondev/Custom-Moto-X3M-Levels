import pygame
from baseObjects import *
import numpy

def makeLandscape(vertices, data):
    baseLandscape = resetBaseLandscape()
    origin = vertices[0]
    print(vertices)
    baseLandscape["params"]["x"] = origin[0]
    baseLandscape["params"]["y"] = origin[1]
    for v in vertices:
        v = numpy.subtract(v,origin)
        baseLandscape["params"]["vertices"].append({"x":v[0],"y":v[1]})
    data["layers"][0].append(baseLandscape)
    print("enter")
    print(data)
    landscapeTemp = []
    return data

def makePipe(vertices, data):
    basePather = resetBaseDynamicPather()
    origin = vertices[0]
    basePather['params']['x'] = origin[0]
    basePather['params']['y'] = origin[1]
    for v in vertices:
        v = numpy.subtract(v, origin)
        basePather["params"]["vertices"].append({"x":v[0],"y":v[1]})
        print(basePather)
    data["layers"][0].append(basePather)
    print("enter")
    print(data)
    return data


def makeFinish(vertices, data):
    baseFinish = resetBaseFinish()
    tL = vertices[0]
    bR = vertices[1]
    C  = [(bR[0]+tL[0])/2,(bR[1]+tL[1])/2]
    
    h = tL[1] - bR[1]
    w = tL[0] - bR[0]
    
    params = baseFinish["params"]

    baseFinish["params"]["x"] = C[0]
    baseFinish["params"]["y"] = C[1]
    baseFinish["params"]["width"] = w
    baseFinish["params"]["height"] = h

    data["layers"][0].append(baseFinish)
    return data

def makeRigidBody(vertices, data):
    baseBody = resetLandscapeShaper()
    sumX = 0
    sumY = 0
    for i in vertices:
        sumX += i[0]
        sumY += i[1]
    origin = (sumX/len(vertices),sumY/len(vertices))
    print("origin: ", origin)
    baseBody['params']['x'] = origin[0]
    baseBody['params']['y'] = origin[1]
    for v in vertices:
        v = numpy.subtract(v, origin)
        baseBody["params"]["vertices"].append({"x":v[0],"y":v[1]})
        print(baseBody)
    data["layers"][0].append(baseBody)
    return data