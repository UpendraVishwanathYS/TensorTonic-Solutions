import numpy as np
from scipy.stats import mode
from collections import Counter

def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    count = dict(Counter(x))

    mode = min({key: value for key, value in count.items() if value == max(count.values())}.keys())
    
    return {'mean':np.mean(x).astype(np.float64), 'median':np.median(x).astype(np.float64), 'mode':float(mode)}