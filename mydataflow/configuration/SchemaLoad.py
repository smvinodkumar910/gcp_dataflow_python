

from .pathconfig import ROOT_DIR
import os
import json


class SchemaLoad :

    #returns schema as dict
    def getSchema(filename:str)->dict:
        r = open(os.path.join(ROOT_DIR, 'configuration' ,'resources', filename))
        data = dict(json.load(r))
        return data
    
    #returns fields names as a list
    def getFieldList(filename:str):
        r = open(os.path.join(ROOT_DIR, 'configuration', 'resources', filename))
        data = dict(json.load(r))
        r.close
        fieldList = list(data.get('fields'))
        listofNames =[]
        for a in fieldList:
            field = dict(a)
            listofNames.append(field.get('name'))
        return listofNames



if __name__ == '__main__':
    SchemaLoad.readfile()