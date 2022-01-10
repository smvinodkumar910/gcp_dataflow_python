

from .pathconfig import ROOT_DIR
import os
import json
import sys

class SchemaLoad :

    def readfile():
        filename = sys.argv[1]
        r = open(os.path.join(ROOT_DIR, 'resources', filename))
        data = dict(json.load(r))
        r.close
        fieldList = list(data.get('fields'))
        listofNames =[]
        for a in fieldList:
            field = dict(a)
            listofNames.append(field.get('name'))
        print(listofNames)

    def getSchema()->dict:
        filename = sys.argv[1]
        r = open(os.path.join(ROOT_DIR, 'resources', filename))
        data = dict(json.load(r))
        return data

def getSchema(filename:str)->dict:
        r = open(os.path.join(ROOT_DIR, 'resources', filename))
        data = dict(json.load(r))
        return data

if __name__ == '__main__':
    SchemaLoad.readfile()