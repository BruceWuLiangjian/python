# -*- coding: utf-8 -*-
def noInformationGainToSplitByID3(dataSet):
        """
        不使用信息增益概念，而是直接判断条件熵的大小
        """
        numFeatures = len(dataSet[0]) -1
        bestConditionEntropy = 1.0
        bestFeature =-1
        for i in range(numFeatures):
                featList = [example[i] for example in dataSet]
                uniqueVals = set(featList)
                conditionEntropy = calcConditionalEntropy(dataSet,i,featList,uniqueVals)
                if (conditionEntropy < bestConditionEntropy):
                        bestConditionEntropy = conditionEntropy
                        bestFeature =i
        return bestFeature

# 决策树的生成改为
dataSet,labels = createDataSet()
myTree = createTree(dataSet,labels,noInformationGainToSplitByID3)
