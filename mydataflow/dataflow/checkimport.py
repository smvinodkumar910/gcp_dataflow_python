
import mydataflow.configuration.pathconfig as config
from mydataflow.configuration.SchemaLoad import SchemaLoad as sl
import os
import mydataflow.Utilities.StringOperations as so
import requests
import json


filename = 'ANNUAL_ENTERPRISE_SURVEY.json'


def httpRequest():
    res = requests.get('https://gorest.co.in/public/v1/users')
    response = dict(res.json()).get('data')
    print(list(response))
    
    
if __name__=='__main__':
    httpRequest()


