import jsonlines
import numpy

articlelength = []
labels = []
with jsonlines.open(r'C:\Users\Krasser Ficker 2.0\Documents\Code\Bachelor\DataPreparation\Dataset\fever2-fixers-dev.jsonl') as f:
    for line in f.iter():
        articlelength.append(line['claim'].count(' ') + 1)
        labels.append(line['label'])


print("Number of Documents: " + str(len(articlelength)))
print("Average Document length: " + str(numpy.average(articlelength)))
print("standard deviation: " + str(numpy.std(articlelength)))
print(len(numpy.unique(labels)))