import trees
mydat,labels=trees.createDataSet()
a=trees.calcShannonEnt(mydat)
print(mydat)
print(labels)
print(a)