import pandas as pd
import math
import numpy 

def getLengthAndDeviationCSV(filepath,textColumn,labelColumn):
    df = pd.read_csv(filepath)
    documentlength = []
    
    for i in (df.iloc[:,textColumn].str.count(' ') + 1):
        documentlength.append(i)
    
    avg = numpy.mean(documentlength)
    devi = numpy.std(documentlength)
    nrUniqueLabels = df.iloc[:,labelColumn].nunique()
    
    return avg, devi, nrUniqueLabels;


