
import re
import os

os.system('cls')

def plot_(path):

    file1 = open(path, 'r')
    Lines = file1.readlines()
    
    count = 0

    find = ['HGF', 'EDCBA', 'clock', 'abcdei', 'fghj']

    listParams = '|'.join(find)

    pattern3 = "\$var reg \d (\W) ({}) \$end".format(listParams)

    pDumpvars = "\$dumpvars"

    pFranco = "^#(\d+)$"

    pValues = ""

    listSymbol_ = []
    listParams_ = []

    listValues = {}

    isOnDump = False

    franco = "0"
    
    for line in Lines:
        count += 1

        textLine = line.strip()

        resultDumpvars = re.match(pDumpvars, textLine)

        if(resultDumpvars):
            print(listSymbol_)
            pValues = "(\w+|\d)\s*({})".format('|'.join(listSymbol_))
            # franco = "0"

            isOnDump = True

        resultFranco = re.match(pFranco, textLine)

        if resultFranco:
            franco = resultFranco.group(1)

        if(isOnDump):
            result3 = re.match(pValues, textLine)

            if result3:
                value = result3.group(1)
                key = result3.group(2)

                KEYwORD = listParams_[listSymbol_.index(key)]

                print(KEYwORD)

                currentvalue = franco + '-' +value

                if(KEYwORD in listValues):
                    preValues = listValues[KEYwORD]
                    listValues[KEYwORD] = preValues + [currentvalue]
                else:
                    listValues[KEYwORD] = [currentvalue]

        else:
            result3 = re.match(pattern3, textLine)

            if result3:
                simbol = result3.group(1)
                param = result3.group(2)

                listSymbol_.append(simbol) if simbol not in listSymbol_ else listSymbol_
                listParams_.append(param) if param not in listParams_ else listParams_


    print('>>> listSymbol_: ', listSymbol_)
    print('>>> listParams_: ', listParams_)

    print('>>> listValues: ', listValues)



plot_('C:\\Users\\JoseK21\\Desktop\\hls\\testbench.vcd')