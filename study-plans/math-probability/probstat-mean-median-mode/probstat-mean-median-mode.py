import numpy as np
from scipy.stats import mode
from collections import Counter
def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    count = dict(Counter(x))

    print(count)

    # print({(key, value) for key, value in count if value == max(count.values())})

    # print({key: value for key, value in count.items() if value == max(count.values())})

    # print(count)
    # smallest_mode = max(count.value(), key = lambda item: (item[1],item[0]))
    smallest_mode = min({key: value for key, value in count.items() if value == max(count.values())}.keys())

    # print(smallest_mode)
    
    return {'mean':np.mean(x).astype(np.float64), 'median':np.median(x).astype(np.float64), 'mode':float(smallest_mode)}


# print(mean_median_mode(x=[1, 1, 2, 3]))