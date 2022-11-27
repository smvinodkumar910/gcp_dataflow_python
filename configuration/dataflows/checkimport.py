
from time import strftime
import configuration.pathconfig as config
from configuration.SchemaLoad import SchemaLoad as sl
import os
import Utilities.StringOperations as so
import requests
import datetime


filename = 'ANNUAL_ENTERPRISE_SURVEY.json'

#yyyy-MM-dd-HHmmss

def httpRequest():
    timenow = (datetime.datetime.now())
    print('ApiToBq-'+timenow.strftime('%Y-%m-%d-%H%M%S'))

    
    
if __name__=='__main__':
    httpRequest()


