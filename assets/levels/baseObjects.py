import json

def resetBaseLandscape():
    return json.loads("""{
                "params": {
                    "direction": 90,
                    "x": 0,
                    "width": 15824,
                    "y": 0,
                    "height": 3046.8,
                    "shape": true,
                    "camera": true,
                    "wireframe": false,
                    "isRoad": true,
                    "line": true,
                    "textureOffset": 0,
                    "smoothing": true,
                    "thick": 128,
                    "stretchTexture": false,
                    "repeatTexture": true,
                    "directed": true,
                    "vertices": [
                        
                    ],
                    "originOffsetRatio": 0,
                    "physic": true,
                    "snapToGrid": false,
                    "straightSides": true,
                    "cameraOffsetY": 120,
                    "textureMode": true,
                    "lineId": 0,
                    "rotation": 0
                },
                "className": "frg.game.editor.objects::GroundPather"
            }""")

def resetBaseDynamicPather():
    return json.loads("""{
                "params": {
                    "x": 0,
                    "graphic": true,
                    "textureOffset": 0,
                    "snapToGrid": true,
                    "height": 1489.2,
                    "wireframe": false,
                    "shapeH": 20,
                    "vertices": [
                    ],
                    "originOffsetRatio": 0,
                    "physic": true,
                    "stretchTexture": false,
                    "straightSides": true,
                    "smoothing": true,
                    "textureMode": true,
                    "type": 2,
                    "width": 207.9,
                    "isStatic": true,
                    "density": "1",
                    "action": 0,
                    "safeId": -1,
                    "id": -1,
                    "rotation": 0,
                    "repeatTexture": true,
                    "y": 0
                },
                "className": "frg.game.editor.objects::DynamicPather"
            }""")

def resetBaseFinish():
    return json.loads(
        """
        {
            "params": {
                "x": 0,
                "width": 0,
                "y": 0,
                "rotation": 0,
                "height": 0
            },
            "className": "FinishZone"
        }
        """
    )

def resetLandscapeShaper(): # layer = 1 is background landscape layer = 2 is landscape object layer = 3 is spikes, layer = 4 is metal block layer 5 is metal background
    return json.loads("""{
                "params": {
                    "safeId": -1,
                    "x": 0,
                    "graphic": true,
                    "ignore": false,
                    "y": 0,
                    "vertices": [
                    ],
                    "physic": true,
                    "layer": 4,
                    "rem": true,
                    "isStatic": false,
                    "density": 1,
                    "line": false,
                    "rotation": 0,
                    "id": -1,
                    "smoothing": true
                },
                "className": "frg.game.editor.objects::LandscapeShaper"
            }""")

def resetPivotJoint():
    return json.loads("""{
                "params": {
                    "x": 0,
                    "width": 17,
                    "y": 0,
                    "height": 17,
                    "safeId": 3,
                    "rotation": 0,
                    "id": 1
                },
                "className": "PivotJointE"
            }""")

def resetTrigger():
    return json.loads("""{
                "params": {
                    "x": 0,
                    "width": 0,
                    "sndId": -1,
                    "y": 0,
                    "height": 0,
                    "hint": -1,
                    "id_off": -1,
                    "safeId": 1,
                    "off": false,
                    "rotation": 0,
                    "id": 1
                },
                "className": "ToggleE"
            }
    
    
    """)

def resetMover():
    return json.loads("""{
                "className": "frg.game.editor.objects::MoverPather",
                "params": {
                    "body": false,
                    "x": 0,
                    "width": 13,
                    "position": 0,
                    "y": 0,
                    "height": 333,
                    "id": 0,
                    "safeId": -1,
                    "cycle": 0,
                    "sideWait": 0,
                    "stopOnPoint": false,
                    "rotation": 0,
                    "sideAngle": 0,
                    "ghostMode": true,
                    "vertices": [
                        
                    ],
                    "snapToGrid": true,
                    "active": 0,
                    "color": {
                        "color": 7340056,
                        "alpha": 1
                    },
                    "startTime": "0",
                    "speed": 840,
                    "stopOnEnd": true,
                    "thickness": 10
                }
            }""")

def resetMotor():
    return json.loads("""{
                "params": {
                    "x": 2570,
                    "graphic": 1,
                    "y": 300,
                    "height": 17,
                    "swoosh": false,
                    "width": 17,
                    "rate": 40,
                    "time": 800,
                    "snd": false,
                    "safeId": -1,
                    "rotation": 0,
                    "id": -1
                },
                "className": "MotorJointE"
            }
    """)

def resetTnt():
    return json.loads("""{    
                "params": {
                    "x": 0,
                    "width": 53.2,
                    "y": 0,
                    "height": 53.2,
                    "physic": false,
                    "count": 40,
                    "stones": false,
                    "impulse": 17000,
                    "radius": 64,
                    "safeId": 3,
                    "rotation": 0,
                    "id": 1
                },
                "className": "Tnt1"
            }""")