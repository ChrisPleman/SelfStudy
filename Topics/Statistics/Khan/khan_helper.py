import numpy as np
from scipy.stats import skewnorm
import seaborn as sns
import matplotlib.pyplot as plt

# Shoutout to the top comment at this link: https://stackoverflow.com/questions/24854965/create-random-numbers-with-left-skewed-probability-distribution
def random_hist(n, maximum, skew, func = np.mean, norm=False, colors={'min': 'k', 'central_measure': 'c', 'max': 'tab:gray'}): # Probably will change to random_hist, cause skew of 0 is likely normal
    skewed_data = skewnorm.rvs(
        a = skew,
        loc = maximum,
        size = n
    )
    
    if norm:
        pass
    
    # ensure no nan values
    skewed_data = skewed_data[np.isnan(skewed_data) == False]
    
    # set min val
    skewed_data -= np.min(skewed_data) # ensure all data points above zero
    
    # obtain metrics
    central_measure = func(skewed_data)
    _min = np.min(skewed_data)
    _max = np.max(skewed_data)
    
    # func_name
    func_name = func.__name__.capitalize()
    print(central_measure)
    print(skewed_data)
    
    # generate hist plot
    sns.histplot(
        skewed_data,
    )

    # add vertical line @ min
    plt.axvline(
        x = _min,
        color=colors['min']
    )

    # add vertical line @ mean
    plt.axvline(
        x = central_measure,
        color=colors['central_measure'],
    )
    
    # add vertical line @ max
    plt.axvline(
        x = _max,
        color=colors['max']
    )

    plt.legend(
        labels=[
            f'Min: {_min:.2f}; {central_measure - _min:.2f} Under Mean',
            f'{func_name}: {central_measure:.2f}',
            f'Max: {_max:.2f}; {_max - central_measure:.2f} Over Mean'
        ]
    )

    plt.title(f'Min, {func_name}, Max of Right Skewed Data');
    
    return skewed_data
    
# https://stackoverflow.com/questions/16330831/most-efficient-way-to-find-mode-in-numpy-array
def mode(arr):
    vals, counts = np.unique(arr, return_counts=True)

    return vals[np.argmax(counts)]