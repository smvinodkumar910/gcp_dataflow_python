
import mydataflow.configuration.pathconfig as config
import os
import re

def runmethod():
    filepath = os.path.join(config.ROOT_DIR,'resources' ,'annual-enterprise-survey-2020.csv' )
    with open(filepath) as file:
        filelines = file.readlines()
    
    row = filelines[1]
    #firstcomma = row.find(',',0,len(row))
    #valuelist = re.split(",(?=(\"[^\"]*\"))",row)
    print(row)
    valuelist=[]
    startind =0
    endind = len(row)
    quotecolstr = 0
    while(True):
        splitind = row.find(',',startind,endind)
        if splitind==-1:
            break;
        else:
            colval = row[startind:splitind]
            if ('"' in colval):
                if(quotecolstr==0):
                    quotecolstr=startind
                    startind=splitind+1
                    continue;
                else:
                    colval = row[quotecolstr:splitind]
                    valuelist.append(colval.replace('"',''))
            else:
                valuelist.append(colval)
            startind=splitind+1

    print(valuelist)
    
    


if __name__ == '__main__':
    runmethod()