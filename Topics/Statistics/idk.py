import numpy as np
from collections import Counter

def _midrange(_list):
    return np.mean([np.max(_list), np.min(_list)])

def _range(_list):
    return np.max(_list) - np.min(_list)

def _mode(_list):
    _counter = Counter(_list)
    _counts = list(_counter.values())
    if np.all(_counts == _counts[0]):
        return 'There is no mode'
    return f'The mode of the dataset is {_counter.most_common(1)[0][0]}'
print(_mode([1,2,1,3]))