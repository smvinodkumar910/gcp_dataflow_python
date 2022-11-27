
from .pathconfig import ROOT_DIR
import os
import json

class AppProperties():

    def getProperty(propertyName:str)->dict:
        r = open(os.path.join(ROOT_DIR, 'resources', 'application.json'))
        data = dict(json.load(r))
        r.close()
        return data.get(propertyName)


if __name__ == '__main__':
    properties = AppProperties.getProperty('gcp')
    print(properties)