import re
import numpy as np
from sequence_lcs_sim import LcsSim

def ModelNumSim(s1, s2):
    numSet1 = set([i for i in re.split(r'\D+', s1) if i])
    numSet2 = set([i for i in re.split(r'\D+', s2) if i])
    print numSet1, numSet2
    if (numSet1 or numSet2) and (not numSet1.intersection(numSet2)):
        return 0
    return LcsSim(s1, s2)
