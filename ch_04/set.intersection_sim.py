#_*_ coding: utf-8 _*_


def IntersectionLength(x, y):
    '''计算两个输入集合的交集长度
       [Parameters]
           x/y： set/list/unicode表示的两个集合
                 string需要先转化为unicode
       [Return]
           <int>: 两个集合的交集长度
    '''
    if not isinstance(x, set):
        x = set(x)
    if not isinstance(y, set):
        y = set(y)
    ins = x.intersection(y)
    return len(ins)


def SetCoverSim(x, y):
    '''计算两个输入集合的覆盖率相似度
       [Parameters]
           x/y： set/list/unicode表示的两个集合
       [Return]
           <float>: 两个集合的覆盖率相似度
    '''
    if not isinstance(x, set):
        x = set(x)
    if not isinstance(y, set):
        y = set(y)
    return IntersectionLength(x, y) * 1.0 / min(len(x), len(y)) 


def JaccardSim(x, y):
    '''计算两个输入集合的Jaccard相似度
       [Parameters]
           x/y： set/list/unicode表示的两个集合
       [Return]
           <float>: 两个集合的Jaccard相似度
    '''
    if not isinstance(x, set):
        x = set(x)
    if not isinstance(y, set):
        y = set(y)
    union = x.union(y)
    return IntersectionLength(x, y) * 1.0 / len(union) 



def DiceSim(x, y):
    '''计算两个输入集合的Dice相似度
       [Parameters]
           x/y： set/list/unicode表示的两个集合
       [Return]
           <float>: 两个集合的Dice相似度
    '''
    if not isinstance(x, set):
        x = set(x)
    if not isinstance(y, set):
        y = set(y)
    return IntersectionLength(x, y) * 2.0 / (len(x) + len(y))



#unit test
if __name__ == '__main__':
    s1 = raw_input("s1:").decode("utf-8")
    s2 = raw_input("s2:").decode("utf-8")
    print IntersectionLength(s1, s2)
    print SetCoverSim(s1, s2)
    print JaccardSim(s1, s2)
    print DiceSim(s1, s2)


