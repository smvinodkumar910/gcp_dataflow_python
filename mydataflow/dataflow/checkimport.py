
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
            print(colval)
            if ('"' in colval):
                if(quotecolstr==0):
                    quotecolstr=startind
                    startind=splitind+1
                    continue;
                else:
                    colval = row[quotecolstr:splitind]
                    valuelist.append(colval.replace('"',''))
                    quotecolstr=0
            else:
                if quotecolstr!=0:
                    startind=splitind+1
                    continue;
                startind=splitind+1
                valuelist.append(colval)
                
            

    print(valuelist)
    
    


if __name__ == '__main__':
    runmethod()