import pygame
from baseObjects import *

def makeLandscape(vertices, data):
    baseLandscape = resetBaseLandscape()
    for v in vertices:
        baseLandscape["params"]["vertices"].append({"x":v[0],"y":v[1]})
    data["layers"][0].append(baseLandscape)
    print("enter")
    print(data)
    landscapeTemp = []
    return data

def makePipe(vertices, data):
    basePather = resetBaseDynamicPather()
    for v in vertices:
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
    for v in vertices:
        baseBody["params"]["vertices"].append({"x":v[0],"y":v[1]})
        print(baseBody)
    data["layers"][0].append(baseBody)
    return data