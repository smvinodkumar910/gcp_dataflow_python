
import mydataflow.configuration.pathconfig as config
from mydataflow.configuration.SchemaLoad import SchemaLoad as sl
import os
import mydataflow.Utilities.StringOperations as so


filename = 'ANNUAL_ENTERPRISE_SURVEY.json'


def csvStringToDict():
    filepath = os.path.join(config.ROOT_DIR,'resources' ,'annual-enterprise-survey-2020.csv' )
    with open(filepath) as file:
        filelines = file.readlines()
    row = filelines[1]
    print(row)
    rowAsDict = process(row)
    #vallist = splitIntoVal(row,',','"')
    #rowAsDict = dict(zip(sl.getFieldList('ANNUAL_ENTERPRISE_SURVEY.json'), vallist))
    #print(row)
    print(rowAsDict)

def process(element:str):
    """Returns an iterator over the words of this element.

    The element is a line of text.  If the line is blank, note that, too.

    Args:
      element: the element being processed

    Returns:
      The processed element.
    """
    colval=[]
    if '"' in element:
      colval=so.splitIntoVal(element,',','"')
    else:
      colval=element.split(',')
      
    fieldList = sl.getFieldList(filename)
    rowAsDict = dict(zip(fieldList, colval))
    return rowAsDict


def splitIntoVal(row:str,delimiter:str,quotechar:str):
    #print(row)
    valuelist=[]
    startind =0
    endind = len(row)
    quotecolstr = 0
    while(True):
        splitind = row.find(delimiter,startind,endind)
        if splitind==-1:
            colval = row[startind:endind-1]
            valuelist.append(colval)
            break;
        else:
            colval = row[startind:splitind]
            #print(colval)
            if (quotechar in colval):
                if(quotecolstr==0):
                    quotecolstr=startind
                    startind=splitind+1
                    continue;
                else:
                    colval = row[quotecolstr:splitind]
                    valuelist.append(colval.replace(quotechar,''))
                    quotecolstr=0
                    startind=splitind+1
            else:
                if quotecolstr!=0:
                    startind=splitind+1
                    continue;
                startind=splitind+1
                valuelist.append(colval)

    return valuelist
    
    
if __name__=='__main__':
    csvStringToDict()


