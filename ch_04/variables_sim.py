#_*_ coding: utf8 _*_


import numpy
from matplotlib.mlab import entropy
from collections import defaultdict

def PearsonSim(X, Y):
    return numpy.corrcoef(X, Y)[0,1]


# def ValueCount(X):
#     hist = deaultdict(lambda: 0)
#     for i in X:
#         hist[i] += 1
# 
# def ValueCount2D(X, Y):
#     hist = defaultdict(lambda: 0)
#     for x in X:
#         for y in Y:
#             hist[(x,y)] += 1


def Entropy(hist, density=False):
    ''' 计算输入分布统计的熵
    [Parameters]
    hist : <numpy array>
            每个值的个数或密度，代表分布函数
    '''
    if not density:
        hist = hist / float(sum(hist))  # coerce to float and normalize
    hist = hist[numpy.nonzero(hist)]            # toss out zeros
    H = -sum(hist * numpy.log(hist))   # compute entropy
    return H


def MutualInfo(x, y, bins):
    '''Compute mutual information'''
    counts_xy = numpy.histogram2d(x, y, bins=bins)[0].flatten()
    counts_x  = numpy.histogram(x, bins=bins)[0]
    counts_y  = numpy.histogram(y, bins=bins)[0]
    H_xy = Entropy(counts_xy)
    H_x  = Entropy(counts_x)
    H_y  = Entropy(counts_y)
    
    return H_x + H_y - H_xy



if __name__ == "__main__":
    a = numpy.random.random_sample(20)
    b = numpy.random.random_sample(20)
    print MutualInfo(a, b, bins=numpy.linspace(0, 1, 1000))