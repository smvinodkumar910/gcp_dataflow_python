




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
    