import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns sample variance and standard deviation as Python floats.
    """
    sum = 0
    for num in x:
        sum+=num
    mean = sum/len(x)
    var = 0
    for num in x:
        var+=(num-mean)**2
        
    var = var/(len(x)-1)
    std = var**(1/2)

    #var = np.std(x,ddof=1)**2; std = np.std(x,ddof=1)
    
    return {'variance':var,'std_dev':std}