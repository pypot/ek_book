#_*_ coding: utf8 _*_

from pu_learning import *

import sklearn
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB

import cPickle as pickle
import numpy
import random


__CONF_MAKE_NEW_DATA__ = False

SAMPLE_CNT = 10000
TRAIN_PROPORTION = 0.8

def MakeUnbalancedSamples(filePath, positive_proportion=0.05):
    '''构造一个不平衡的测试集
    '''
    X, Y = datasets.make_classification(n_samples=SAMPLE_CNT, n_features=30, n_informative=20,
                                        n_redundant=2, n_repeated=0, n_classes=2,
                                        weights=[1-positive_proportion, positive_proportion],
                                        n_clusters_per_class=1, flip_y=0.01)
    Y.resize((SAMPLE_CNT, 1))
    data = numpy.hstack((Y, X))
    numpy.savetxt(open(filePath, 'w'), data)
    
    
def ReadUnbalancedSamples(filePath, label_recall=0.5):
    '''返回值 label_positive, unlabeled 用于学习
       real_negative, lost_positive 用于测试
    '''
    data = numpy.loadtxt(open(filePath))
    real_positive = data[data[:, 0] == 1][:, 1:].copy()
    real_negative = data[data[:, 0] == 0][:, 1:].copy()
    random.shuffle(real_positive)
    label_cnt = len(real_positive) * label_recall
    label_positive = real_positive[:label_cnt].copy()
    lost_positive = real_positive[label_cnt:].copy()
    unlabeled = numpy.vstack((real_negative, lost_positive)).copy()
    #random.shuffle(unlabeled)
    
    #print lost_positive == real_positive[label_cnt:]
#     print len(unlabeled)
#     print len([i for i in unlabeled if i in numpy.vstack((real_negative, lost_positive))])
    return label_positive, unlabeled, real_negative, lost_positive


if __name__ == "__main__":
    DATA_PATH = "data/pu_learn_data1.txt"
    if __CONF_MAKE_NEW_DATA__:
        MakeUnbalancedSamples(DATA_PATH)
    a, b, c, d = ReadUnbalancedSamples(DATA_PATH)
    print len(a), len(b), len(c), len(d)
    trainX = numpy.vstack((a, b))
    trainY = numpy.hstack(( numpy.ones(len(a)), numpy.zeros(len(b)) ))
    est = PU_RealNegativeFinder()
    n = est.find_real_negative(trainX, trainY)
    print len(n)
    print len([i for i in b if i in n])
    print len([i for i in c if i in n])
    print len([i for i in d if i in n])
#     print sum(est.predict(b) < 0) 
#     print sum(est.predict(c) < 0) 
#    print sum(est.predict(d) < 0) 
