#_*_ coding: utf8 _*_

import sklearn
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB

import cPickle as pickle
import numpy
import random

SAMPLE_CNT = 10000
TRAIN_CNT = 8000


def PatitionalLabel(Y):
    return numpy.hstack((Y[:len(Y)/2], numpy.zeros(len(Y) - len(Y)/2)))
 

class PU_Samples(object):
    def __init__(self, positive=None, unlabeled=None):
        self.positive = positive
        self.unlabeled = unlabeled
        self.negative = None
        self.spy = None
        self.train_positive = None
        self.train_negative = None
        
    


class PU_RealNegativeFinder(object):
    def __init__(self, core_estimator="", core_parameters=None, spy_proportion=0.20, thres_level=0.05, iter_times=5):
        #self.core_estimator = BernoulliNB()
        self.core_estimator = LogisticRegression()
        self.spy_proportion = spy_proportion
        self.thres_level = thres_level
        self.iter_times = iter_times
        self.real_negative_ = None
        self.data_buf_ = None
        self.proba_thres_ = 0
        

    def _spy_sampling(self):
        random.shuffle(self.data_buf_.positive)
        spyCnt = len(self.data_buf_.positive) * self.spy_proportion
        self.data_buf_.spy = self.data_buf_.positive[:spyCnt]
        self.data_buf_.train_positive = self.data_buf_.positive[spyCnt:]
        self.data_buf_.train_negative = numpy.vstack((self.data_buf_.unlabeled, self.data_buf_.spy))
        
    
    def _core_fit(self):
        trainX = numpy.vstack((self.data_buf_.train_positive, self.data_buf_.train_negative))
        trainY = numpy.hstack((numpy.ones(len(self.data_buf_.train_positive)), numpy.zeros(len(self.data_buf_.train_negative)) ))
        self.core_estimator.fit(trainX, trainY)
        
        
    def _find_negative(self):
        spy_probas = self.core_estimator.predict_proba(self.data_buf_.spy)[:, 1]
        thres_pos = len(self.data_buf_.spy) * self.thres_level
        spy_probas.sort()
        self.proba_thres_ = spy_probas[thres_pos]
        print self.proba_thres_ 
        unlabeled_probas = self.core_estimator.predict_proba(self.data_buf_.unlabeled)[:, 1]
        #self.data_buf_.negative = self._array_intersect(self.data_buf_.negative, 
        #                                                self.data_buf_.unlabeled[unlabeled_probas < self.proba_thres_])
        self.real_negative_ = self._array_intersect(self.real_negative_, 
                                                    self.data_buf_.unlabeled[unlabeled_probas < self.proba_thres_])
        #self.real_negative_ = self.data_buf_.unlabeled[unlabeled_probas < self.proba_thres_]
        print "IN", len(self.real_negative_), len(self.data_buf_.unlabeled)

    
    def _array_intersect(self, a, b):
        if a == None:
            return b
        return numpy.array([i for i in a if i in b])

    
    def fit(self, X, Y):
        self.data_buf_ = PU_Samples(X[Y == 1], X[Y == 0])
        self._spy_sampling()
        self._core_fit()
        self._find_negative()
        
        
    def predict(self, X):
        Y = numpy.zeros(len(X))
        Y[self.core_estimator.predict_proba(X)[:, 1] < self.proba_thres_] = -1 
        return Y
    
    
    def find_real_negative(self, X, Y):
        self.real_negative_ = X[Y == 0]
        self.data_buf_ = PU_Samples(X[Y == 1], X[Y == 0])
        for i in xrange(self.iter_times):
            self._spy_sampling()
            self._core_fit()
            self._find_negative()
        return self.real_negative_
        
        



