#_*_ coding: utf8 _*_

import sklearn
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB

import cPickle as pickle
import numpy

SAMPLE_CNT = 5000

def MakeUnbalanceSamples(filePath):
    X, Y = datasets.make_classification(n_samples=SAMPLE_CNT, n_features=25, n_informative=10,
                                        n_redundant=2, n_repeated=0, n_classes=2,
                                        n_clusters_per_class=4, weights=[0.95, 0.05], flip_y=0.01)
    Y.resize((SAMPLE_CNT, 1))
    data = numpy.hstack((Y, X))
    numpy.savetxt(open(filePath, 'w'), data)


def PatitionalLabel(Y):
    return numpy.hstack((Y[:len(Y)/2], zeros(len(Y) - len(Y)/2)))
 

class PuEstimator(object):
    def __init__(self):
        self.core_estimator = None
    
    def split_samples(self, X, Y):
        positiveSamples = X[Y==1]
        unlabeledSamples = X[Y==0]
        spyCnt = len(posSamples) * 0.15
        spySamples = posSamples[ : spyCnt]
        trainPosSamples = posSamples[spyCnt : ]
        trainX = numpy.hstack((trainPosSamples, spySamples, unlabeledSamples))
        trainY =  numpy.hstack((ones(len(trainPosSamples)), zeors(len(spySamples)), zeors(len(unlabeledSamples)))
    
    def fit(self, X, Y):
        X[Y == 1]



#debug
if __name__ == "__main__":
    DATA_FILE = r"D:\1.npy"
    #MakeUnbalanceSamples(DATA_FILE)
    data = numpy.loadtxt(open(DATA_FILE))
    trueY = data[:, 0]
    partY = PatitionalLabel(trueY)
    X = data[:, 1:]
    estimatorA = LogisticRegression()
    estimatorA.fit(X, partY)
    estimatorB = BernoulliNB()
    estimatorB.fit(X, partY)
    print len(X[partY==1])
    P = estimatorA.predict_proba(X[partY==1])
    print P[P>0]
    