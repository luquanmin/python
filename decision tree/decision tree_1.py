import numpy as np
from functools import reduce
from sklearn.naive_bayes import MultinomialNB

def loadDataSet():
    postingList = [['my', 'dog', 'has','flea', 'problems','help','please'],
                   ['maybe','not','take','him','to','dog','park','stupid'],
                   ['my','dalmation','is','so','cute','I','love','him'],
                   ['stop','posting','stupid','worthless','garbage'],
                   ['mr','licks','ate','my','steak','how','to','stop','him'],
                   ['quit','buying','worthless','dog','food','stupid']]
    classVec = [0,1,0,1,0,1]
    return postingList, classVec

def createVocabList(dataSet):
    vocabSet= set([])  #创建一个空的不重复列表
    for document in dataSet:
        vocabSet=vocabSet|set(document) #取并集
    #print(vocabSet)
    #print(len(vocabSet))
    return list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):
    returnVec= [0]*len(vocabList)
    #print(returnVec)
    #print(len(returnVec))
    for word in inputSet:
        #print(word)
        #print('\t')
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
            #print(returnVec)
        else:
            print("词汇：%s 并没有在词汇表中" % word)
    #print(returnVec)
    #print(type(returnVec))
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    # print(trainMatrix)
    # print(trainCategory)
    # print(sum(trainCategory))
    # print(numTrainDocs)
    # print(float(numTrainDocs))
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # print(pAbusive)
    p0Num = np.ones(numWords);
    p1Num = np.ones(numWords)
    # print(numWords)
    # print(p0Num)
    # print(p1Num)
    p0Denom1 = [0] * numWords;
    p1Denom1 = [0] * numWords
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            # print(p1Num)
            # print('\t')
            p1Denom1 += trainMatrix[i]
            # print('\t')
            # print('\t')
            # print(len(p1Denom1))
        else:
            p0Num += trainMatrix[i]
            p0Denom1 += trainMatrix[i]

    print(p1Denom1)
    # print(p0Denom1)
    print(numWords - list(p1Denom1).count(0))
    print(numWords - list(p0Denom1).count(0))
    p0Denom0 = numWords;
    p1Denom0 = numWords

    p0Denom = p0Denom0 + (numWords - list(p1Denom1).count(0));
    p1Denom = p1Denom0 + (numWords - list(p0Denom1).count(0));
    p1Vect = np.log(p1Num / p1Denom)
    p0Vect = np.log(p0Num / p0Denom)
    # p1Vect = p1Num/p1Denom
    # p0Vect = p0Num/p0Denom

    # print(p1Vect)
    # print(p0Vect)

    # print(sum(p1Vect))
    # print(sum(p0Vect))
    return p0Vect, p1Vect, pAbusive

def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    print(vec2Classify)
    print(type(vec2Classify))
    print(p1Vec)
    print(type(p1Vec))
    print(vec2Classify*p1Vec)
    p1=sum(vec2Classify*p1Vec)+np.log(pClass1)
    p0=sum(vec2Classify*p0Vec)+np.log(1.0-pClass1)
    print('p0:',p0)
    print('p1:',p1)
    if p1>p0:
        return 5
    else:
        return 0


def testingNB():
    list0Posts, listClasses = loadDataSet()
    # print(list0Posts)
    myVocabList = createVocabList(list0Posts)
    # print(myVocabList)
    # print(len(myVocabList))
    trainMat = []
    for postinDoc in list0Posts:
        # print(postinDoc)
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
        # print(trainMat)
        # print(len(trainMat))
        # print(trainMat)
        # print('\t')
    p0V, p1V, pAb = trainNB0(np.array(trainMat), np.array(listClasses))
    # print(np.array(trainMat))
    # print(np.array(trainMat).shape)
    # print(len(np.array(trainMat)))
    # print(np.array(listClasses))

    testEntry1 = ['love', 'my', 'dalmation']
    thisDoc1 = np.array(setOfWords2Vec(myVocabList, testEntry1))
    if classifyNB(thisDoc1, p0V, p1V, pAb):
        print(testEntry1, '属于侮辱类')
    else:
        print(testEntry1, '属于非侮辱类')

    testEntry2 = ['stupid','garbage']
    thisDoc2 = np.array(setOfWords2Vec(myVocabList, testEntry2))
    if classifyNB(thisDoc2,p0V,p1V,pAb):
    print(testEntry2,'属于侮辱类')
    else:
    print(testEntry2,'属于非侮辱类')


if __name__ == '__main__':
    testingNB()
https://tianchi.aliyun.com/course/288/3407