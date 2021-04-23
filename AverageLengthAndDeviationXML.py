import xml.etree.ElementTree as ET
import os
import math
import numpy

directory =  os.listdir(r'C:\Users\Krasser Ficker 2.0\Documents\Code\Bachelor\DataPreparation\Dataset')
directoryname = r'C:\Users\Krasser Ficker 2.0\Documents\Code\Bachelor\DataPreparation\Dataset'

articlelength = []
for file in directory:
    filename = os.fsdecode(file)
    filepath = directoryname+'\\'+filename
    if filename.endswith(".xml"):
        tree = ET.parse(filepath)
        root = tree.getroot()
        if not root.find('mainText').text is None:
            articlelength.append(root.find('mainText').text.count(' ') + 1)

print("Number of Documents: " + str(len(articlelength)))
print("Average Document word count: " + str(numpy.average(articlelength)))
print("Standard Deviation of Document word count: " + str(numpy.std(articlelength)))
