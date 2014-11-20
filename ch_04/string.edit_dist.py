#_*_coding:utf-8_*_

import numpy as np
#使用numpy的数组来记录已经解过的子问题

def EditDist(x, y):
    '''计算两个输入字符串的编辑距离
       [Parameters]
           x/y： 用string或unicode表示的两个字符串
       [Return]
           <int>: 两个输入字符串的编辑距离
    '''
    lenx = len(x)
    leny = len(y)
    #recMatrix用来存放已经解过的子问题
    recMatrix = np.zeros((lenx+1, leny+1), dtype=int)

    #记录边界条件
    recMatrix[:, 0] = range(lenx+1)
    recMatrix[0, :] = range(leny+1)

    for m in xrange(lenx):
        for n in xrange(leny):
            #cmpList用来存放候选的子问题推导式
            cmpList = [recMatrix[m, n+1] + 1, recMatrix[m+1, n] + 1]
            if m >= 1 and n >= 1 and x[m-1] == y[n] and x[m] == y[n-1] :
                cmpList.append(recMatrix[m-1, n-1] + 1)
            if x[m] == y[n]:
                cmpList.append(recMatrix[m, n])
            else:
                cmpList.append(recMatrix[m, n]+1)
            #从候选集中选出最优值
            recMatrix[m+1, n+1] = min(cmpList)
    return recMatrix[lenx, leny]

def NormEditDist(x, y):
    '''返回标准化的编辑距离
    '''
    return EditDist(x, y) * 1.0 / max(len(x), len(y))


#unit test
if __name__ == '__main__':
    s1 = raw_input("s1:").decode("utf-8")
    s2 = raw_input("s2:").decode("utf-8")
    print EditDist(s1, s2)
    print NormEditDist(s1, s2)
