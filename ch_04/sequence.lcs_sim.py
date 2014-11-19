#_*_ coding: utf-8 _*_

import numpy as np

def LcsLength(x, y):
    '''计算两个序列的最长公共子序列(Longgest Common Sequence)长度
    [Parameters]
        x/y： 用list, numpy arry, string 或unicode表示的两个序列
    [Return]
       <int>: 两个输入序列的最长公共子序列长度
    '''
    lenx = len(x)
    leny = len(y)
    recMatrix = np.zeros((lenx+1, leny+1), dtype=int)

    for m in xrange(lenx):
        for n in xrange(leny):
            if x[m] == y[n]:
                recMatrix[m+1, n+1] = recMatrix[m, n] + 1
            else:
                recMatrix[m+1, n+1] = max(recMatrix[m, n+1], recMatrix[m+1, n])
    return recMatrix[lenx, leny]


def LcsSim(x, y):
    '''计算两个unicode串的LCS相似度
    [Parameters]
        x/y： unicode编码的两个字符串
    [Return]
       <float>: LCS相似度
    '''
    return LcsLength(x, y) * 1.0 / min(len(x), len(y))


#unit test
if __name__ == '__main__':
    s1 = [1, 2, 3, 4, 5, 6, 7]
    s2 = [3, 3, 5, 1, 7, 1]
    print LcsLength(s1, s2)
    print LcsSim(s1, s2)
    s1 = raw_input("s1:").decode("utf-8")
    s2 = raw_input("s2:").decode("utf-8")
    print LcsLength(s1, s2)
    print LcsSim(s1, s2)
