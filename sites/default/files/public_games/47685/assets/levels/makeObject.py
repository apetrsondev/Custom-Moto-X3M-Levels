import pygame
from baseObjects import *
import numpy
import easygui

# data["layers"][0] is the landscape 
# data["layers"][1] contain decorations
# data["layers"][2] contain barrels/tnt  ?? EggE may be sawblade
# data["layers"][3] is a second Decoration Category?? maybe??
# data["layers"][4] is the player respawn points/checkpoints 
# data["layers"][5] MAY BE TRIGGER SHIT


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
    # Layer 0: supposed to be wood but throws error
    # Layer 1: background dirt
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


def makePivotJoint(vertex, data):
    basePivot = resetPivotJoint()
    basePivot['params']['x'] = vertex[0]
    basePivot['params']['y'] = vertex[1]
    ID = easygui.integerbox("Enter ID", "ID PROMPT", -1)
    basePivot['params']['id'] = ID
    data['layers'][0].append(basePivot)
    return data

def makeTrigger(vertices, data):
    baseTrigger = resetTrigger()
    tL = vertices[0]
    bR = vertices[1]
    C  = [(bR[0]+tL[0])/2,(bR[1]+tL[1])/2]
    
    h = tL[1] - bR[1]
    w = tL[0] - bR[0]
    
    # params = baseFinish["params"]

    ID = easygui.integerbox("Enter ID", "ID PROMPT")
    print(ID)
    baseTrigger["params"]["x"] = C[0]
    baseTrigger["params"]["y"] = C[1]
    baseTrigger["params"]["width"] = w
    baseTrigger["params"]["height"] = h
    baseTrigger["params"]['id'] = ID
    data["layers"][5].append(baseTrigger)
    return data

def makeMover(vertices, data):
    baseMover = resetMover()
    origin = vertices[0]
    baseMover['params']['x'] = origin[0]
    baseMover['params']['y'] = origin[1]
    for v in vertices:
        v = numpy.subtract(v, origin)
        baseMover["params"]["vertices"].append({"x":v[0],"y":v[1]})
        print(baseMover)
    ID = easygui.integerbox("Enter ID", "ID PROMPT")
    speed = easygui.integerbox("Enter speed (launcher on 21 is 840)", "Speed PROMPT", 800, upperbound=2000)
    waitTime = easygui.integerbox("Enter Wait Time (secs)", "Wait PROMPT", 0)
    baseMover['params']['id'] = ID
    baseMover['params']['speed'] = speed
    baseMover['params']['startTime'] = waitTime
    data["layers"][5].append(baseMover)

    # print("enter")
    # print(data)
    return data

def makeMotor(vertex, data):
    baseMotor = resetMotor()
    baseMotor['params']['x'] = vertex[0]
    baseMotor['params']['y'] = vertex[1]
    ID = easygui.integerbox("Enter ID", "ID PROMPT", -1)
    speed = easygui.integerbox("Enter speed (wheels on 3 are 40) (negative number for counter-clockwise) ", "speed prompt", 100, upperbound=2000)
    baseMotor['params']['id'] = ID
    baseMotor['params']['rate'] = speed
    data['layers'][5].append(baseMotor)
    return data

def makeTnt(vertex, data):
    baseTnt = resetTnt()
    baseTnt["params"]['x'] = vertex[0]
    baseTnt["params"]['y'] = vertex[1]
    ID = easygui.integerbox("Enter ID", "ID PROMPT")
    radius = easygui.integerbox("Enter radius of explosion:", "Enter Radius", 64,0,None)
    power = easygui.integerbox("Enter power of explosion:", "Enter Power", 10000,0,None)
    isPhysics = easygui.boolbox("Make it rigid body?", "make rigid body")
    baseTnt['params']['radius'] = radius
    baseTnt['params']['id'] = ID
    baseTnt['params']['impulse'] = power
    baseTnt['params']['physic'] = isPhysics
    data['layers'][2].append(baseTnt)
    return data
