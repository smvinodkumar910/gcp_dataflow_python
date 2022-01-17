
from time import strftime
import mydataflow.configuration.pathconfig as config
from mydataflow.configuration.SchemaLoad import SchemaLoad as sl
import os
import mydataflow.Utilities.StringOperations as so
import requests
import datetime


filename = 'ANNUAL_ENTERPRISE_SURVEY.json'

#yyyy-MM-dd-HHmmss

def httpRequest():
    timenow = (datetime.datetime.now())
    print('ApiToBq-'+timenow.strftime('%Y-%m-%d-%H%M%S'))

    
    
if __name__=='__main__':
    httpRequest()


