import os
import json 
import pygame
import numpy
import codecs
from math import *
from baseObjects import *
import makeObject as mo

pygame.init()
name = "level maker (beta)"
pygame.display.set_caption(name)
# os.system("touch customLevel.json")
baseFile = open("base.json", encoding= "utf-8-sig")
# baseFile = codecs.open("map2.json", encoding= "utf-8-sig")
# newFile = codecs.open("customLevel.json", encoding= "utf-8-sig", mode = "w")
baseJson = baseFile.read()
# newFile.write(baseJson)

text = baseJson

data = json.loads(text)



resolution = (1000,1000)
SCREEN = pygame.display.set_mode(resolution, pygame.RESIZABLE)

SCREEN.fill((0,0,0))

data = json.loads(text)

pygame.display.flip()

objectList = []
objectName = []
objectListHW = []
objectHWName = []

# baseFinish = resetBaseFinish()
# baseLandscape = resetBaseLandscape()

objectList     = []
objectListHW   = []
objectName     = []
objectHWName   = []
objectIDHW     = []
objectID       = []
objectHWRadius = []

def getObjects(layers):
            for i in layers:
                # print(i["className"])
                try:
                    x = int(i["params"]["x"])
                    y = int(i["params"]["y"])
                except:
                    continue

                # print(x,y)
                globalPos = []
                try: 
                    for v in i["params"]["vertices"]:
                        # print("X/Y",v["x"], v["y"])
                        localx = int(v["x"])
                        localy = int(v["y"])
                        rotation = i["params"]["rotation"]

                        rotation = radians(rotation)
                        
                        cos_r = cos(rotation)
                        sin_r = sin(rotation)
                        arr = numpy.array([[cos_r, -sin_r],[sin_r, cos_r]])

                        coords = numpy.array([localx,localy]).dot(arr.T)

                        localx = coords[0]
                        localy = coords[1]

                        globalPos.append([localx + x, localy + y, i["params"]["rotation"]])
                    objectList.append(globalPos)
                    objectName.append(i["className"])
                    # objectList.append
                    try:
                        objectID.append(i["params"]['id'])
                    except:
                        objectID.append(-2)
                except:
                    # print("H/W",i["params"]["height"], i["params"]["width"])
                    objectListHW.append((x,y,i["params"]["height"], i["params"]["width"],i["params"]["rotation"]))
                    objectHWName.append(i["className"])
                    try:
                        objectIDHW.append(i['params']['id'])
                    except:
                        objectIDHW.append(-2)
                    try:
                        objectHWRadius.append(i['params']['radius'])
                    except:
                        objectHWRadius.append(-1)
                # print(globalPos)
                # print("\n")
            return objectList, objectListHW, objectName, objectHWName, objectHWRadius

# * data["layers"][0] is the landscape 
# * data["layers"][1] contain decorations
# * data["layers"][2] contain barrels/tnt # ? EggE is a mystery
# * data["layers"][3] is a second Decoration Category?? maybe??
# * data["layers"][4] is the player respawn points/checkpoints 
# * data["layers"][5] MAY BE TRIGGER SHIT

zoomV = 1
moveV = [0,0]

landscapeTemp = []

def updateLayers():
    layers = data["layers"][0]

    decLayer = data["layers"][1]
    try:
        layer5 = data["layers"][5]
    except:
        layer5 = None
    checkpoints = data["layers"][4]
    tnt = data["layers"][2]
    mystery = data["layers"][3]

    if decLayer != None:
        decs = getObjects(decLayer)
    if layer5 != None:
        triggers = getObjects(layer5)
    if tnt != None:
        tntLayer = getObjects(tnt)
    if mystery != None:
        mysteryLayer = getObjects(mystery)
    # try:
    #     print("2nd Decoration Successful!")
    # except:
        # pass
    if checkpoints != None:
        savepoints = getObjects(checkpoints)

    # try:


    OBJ = getObjects(layers)
    # objectList = OBJ[0]
    # objectListHW = OBJ[1]
    # objectName = OBJ[2]
    # objectHWName = OBJ[3]

    return OBJ

OBJ = updateLayers()

objectList = OBJ[0]
objectListHW = OBJ[1]
objectName = OBJ[2]
objectHWName = OBJ[3]
objectHWRadius = OBJ[4]

font = pygame.font.Font(None, 20)

vertex = pygame.image.load("vertices.png")
timer = pygame.time.Clock()
while True:
    timer.tick(60)
    SCREEN.fill((0,0,0))
    for v in landscapeTemp: # place vertices for selected object
        SCREEN.blit(vertex, [(moveV[0]+v[0])*zoomV,(moveV[1]+v[1])*zoomV])
    if len(landscapeTemp) >= 2: # place lines for current object
        landscapeTempG = []
        for v in landscapeTemp:
            landscapeTempG.append(numpy.multiply(numpy.add(v,moveV),zoomV))
        pygame.draw.lines(SCREEN, (0,255,0), False, landscapeTempG)

    for v in objectListHW: # render all rectangles
        rec = pygame.rect.Rect(zoomV*(v[0] + moveV[0]), zoomV*(v[1] + moveV[1]), v[3]*zoomV, v[2]*zoomV)
        rec.center = (zoomV*(v[0] + moveV[0]), zoomV*(v[1] + moveV[1]))
        
        x = v[0]
        y = v[1]
        w = v[2]
        h = v[3]
        r = v[4]

        # zoomV = 1
        if objectHWName[objectListHW.index(v)] == "frg.game.editor.objects::DynamicPather":
            color = (255,0,0)
        else:
            color = (255,255,255)

        r= radians(r) + pi/2
        # print(r)
        topL = (int(((w/2)*cos(r)-(h/2)*sin(r))*zoomV),int(((w/2)*sin(r)+(h/2)*cos(r))*zoomV))
        topR = (int(-((w/2)*cos(r)+(h/2)*sin(r))*zoomV),int(-((w/2)*sin(r)-(h/2)*cos(r))*zoomV))
        bottomL = (-1*topR[0], -1*topR[1])
        bottomR = (-1*topL[0], -1*topL[1])
        
        if objectHWName[objectListHW.index(v)] == "Tnt1":
            pygame.draw.circle(SCREEN, color, rec.center, objectHWRadius[objectListHW.index(v)]*zoomV, 1)

        pygame.draw.lines(SCREEN,color,False, ((rec.center[0]+topR[0],rec.center[1]+topR[1]), (rec.center[0]+topL[0],rec.center[1]+topL[1]), (rec.center[0]+bottomL[0], rec.center[1]+bottomL[1]), (rec.center[0]+bottomR[0],rec.center[1]+bottomR[1]), (rec.center[0]+topR[0],rec.center[1]+topR[1]), (rec.center[0]+bottomL[0], rec.center[1]+bottomL[1])))
        ID = font.render(f'{objectIDHW[objectListHW.index(v)]}',True, (0,255,0))
        print(rec.center)
        SCREEN.blit(ID, (rec.center[0]+bottomL[0],rec.center[1]+bottomL[1]))

    for item in objectList:
        try:
            if objectName[objectList.index(item)] == "frg.game.editor.objects::DynamicPather":
                color = (255,0,0)
            else:
                color = (255,255,255)
        except:
            color = (255,0,255)
        if len(item) == 0:
            continue
        vOG = item[0]
        for v in item:
            SCREEN.blit(vertex, [(v[0] + moveV[0])*zoomV - 1,(v[1] + moveV[1])*zoomV - 1])
            pygame.draw.line(SCREEN,color,[int(zoomV*(vOG[0] + moveV[0])),int((vOG[1]+moveV[1])*zoomV)],[int((v[0] + moveV[0])*zoomV), int((v[1] + moveV[1])*zoomV)])
            vOG = v
        ID = font.render(f"{objectID[objectList.index(item)]}", True, (0,255,0))
        SCREEN.blit(ID, [(item[0][0]+moveV[0])*zoomV - 1, (item[0][1]+moveV[1])*zoomV + 15])
        # print("FONT POS", [(item[0][0]+moveV[0])*zoomV - 1, (item[0][1]+moveV[1])*zoomV + 15])
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                json_object = json.dumps(data, indent = 4)
                # os.system("rm -f map1.json")
                # os.system("touch map1.json")
                newFile = codecs.open("map1.json", encoding= "utf-8-sig", mode = "w")
                # newFile.write("")
                newFile.write(json_object)
                newFile.close()
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                landscapeTemp.append([(pygame.mouse.get_pos()[0]/zoomV-moveV[0]),(pygame.mouse.get_pos()[1]/zoomV-moveV[1])])  # * i dont kmow why its - instead of + but it works T-T
                print(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if len(landscapeTemp) == 1:
                    if event.key == pygame.K_n:
                        data = mo.makePivotJoint(landscapeTemp[0], data)
                        landscapeTemp = []
                        updateLayers()
                    elif event.key == pygame.K_m:
                        data = mo.makeMotor(landscapeTemp[0], data)
                        landscapeTemp = []
                        updateLayers()
                    elif event.key == pygame.K_t:
                        data = mo.makeTnt(landscapeTemp[0],data)
                        landscapeTemp = []
                        updateLayers()
                if len(landscapeTemp) >= 2:
                    if event.key == pygame.K_RETURN:
                        data = mo.makeLandscape(landscapeTemp, data)
                        landscapeTemp = []
                        updateLayers()
                    elif event.key == pygame.K_p:
                        data = mo.makePipe(landscapeTemp, data)
                        landscapeTemp = []
                        updateLayers()
                    elif event.key == pygame.K_d:
                        data = mo.makeRigidBody(landscapeTemp, data)
                        updateLayers()
                        landscapeTemp = []
                    elif event.key == pygame.K_m:
                        data = mo.makeMover(landscapeTemp, data)
                        updateLayers()
                        landscapeTemp = []
                    elif len(landscapeTemp) == 2:
                        if event.key == pygame.K_f: # * making finish
                            data = mo.makeFinish(landscapeTemp, data)
                            updateLayers()
                            landscapeTemp = []
                        elif event.key == pygame.K_t:
                            data = mo.makeTrigger(landscapeTemp, data)
                            updateLayers()
                            landscapeTemp = []



                if keys[pygame.K_LCTRL] and (event.key == pygame.K_z) and len(landscapeTemp) > 0:
                    landscapeTemp.pop()
                if event.key == pygame.K_EQUALS:
                    zoomV *= 2
                    print("+")
                if event.key == pygame.K_MINUS:
                    zoomV /= 2

    if keys[pygame.K_RIGHT]:
        moveV[0] -= 20 * (1/zoomV)
    elif keys[pygame.K_LEFT]:
        moveV[0] += 20 * (1/zoomV)
    if keys[pygame.K_UP]:
        moveV[1] += 20 * (1/zoomV)
    if keys[pygame.K_DOWN]:
        moveV[1] -= 20 * (1/zoomV)

    
    pygame.display.flip()

# print(data)
# import http

# http.server
