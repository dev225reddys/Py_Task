import json

def readJson(jsonFile):
    rJson = open(jsonFile)
    getJsonData = json.load(rJson)
    return getJsonData