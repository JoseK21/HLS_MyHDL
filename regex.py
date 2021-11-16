
import re
import os

os.system('cls')

def plot_(pathname):
    if(os.path.isfile(pathname)):
        fileVCD = open(pathname, 'r')
        lineText = fileVCD.readlines()
        
        count = 0

        regexReg_Symbol_Signal = "\$var reg \d (\W) (\w+) \$end"
        regexSearch_By_Symbol = "(\w+|\d)\s*(\W)"
        regexEdges_Clock = "^#(\d+)$"
        regexDumpvars = "\$dumpvars"

        arraySymbols = []
        arraySignals = []

        listValues = {}

        isOnDump = False

        lastEdgeValue = "0"
        
        for line in lineText:
            count += 1
            textLine = line.strip()

            hasMatch_With_Dumpvars = re.match(regexDumpvars, textLine)
            hasMatch_With_Edge = re.match(regexEdges_Clock, textLine)

            if(hasMatch_With_Dumpvars):
                isOnDump = True

            if hasMatch_With_Edge:
                lastEdgeValue = hasMatch_With_Edge.group(1)

            # Lectura de la data para generar las senales visuales
            if(isOnDump):
                hasMatch_Searching_Symbol = re.match(regexSearch_By_Symbol, textLine)

                if hasMatch_Searching_Symbol:
                    valueDump = hasMatch_Searching_Symbol.group(1)
                    symbolDump = hasMatch_Searching_Symbol.group(2)

                    if(symbolDump in arraySymbols):
                        KEYwORD = arraySignals[arraySymbols.index(symbolDump)]

                        currentvalue = lastEdgeValue + '-' +valueDump

                        if(KEYwORD in listValues):
                            preValues = listValues[KEYwORD]
                            listValues[KEYwORD] = preValues + [currentvalue]
                        else:
                            listValues[KEYwORD] = [currentvalue]
    
            # Analisis de variables utilizadas 
            else:
                hasMatch_With_Symbol_Signal = re.match(regexReg_Symbol_Signal, textLine)

                if hasMatch_With_Symbol_Signal:
                    _symbol_ = hasMatch_With_Symbol_Signal.group(1)
                    _signal_ = hasMatch_With_Symbol_Signal.group(2)

                    if(_signal_ not in arraySignals):
                        arraySignals.append(_signal_) if _signal_ not in arraySignals else arraySignals
                        arraySymbols.append(_symbol_) if _symbol_ not in arraySymbols else arraySymbols

        return [arraySignals, arraySymbols, listValues, lastEdgeValue]
    else:
        return [[], [], {},  "-1"]

# plot_('C:\\Users\\JoseK21\\Desktop\\hls\\testbench.vcd')