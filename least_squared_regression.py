# import warnings
import logging
logging.basicConfig(filename="debug.log",format='%(asctime)s - %(message)s', level=logging.WARNING)


try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # Import Dataset
    data = pd.read_csv('dataset.csv')
    print(data)
    
    # raise warnings.warn(RuntimeWarning)

    x = np.array(data['x'])
    y = np.array(data['y'])
    e = np.array(data['e'])

    p = np.sum(1 / e**2)
    q = np.sum(x / e**2)
    r = np.sum(y / e**2)
    s = np.sum(x**2 / e**2)
    t = np.sum(x*y / e**2)

    delta = p*s - q**2

    a = (r*s - q*t)/ delta
    b = (p*t - q*r)/ delta

    std_dev_a = np.sqrt(s/delta)
    std_dev_b = np.sqrt(p/delta)

    print("Best-Fit Parameters")
    print("p: " + str(p) + "\t q: " + str(q) + "\t r: " + str(r) + "\t s: " + str(s) + "\t t: " + str(t))
    print("Delta: " + str(delta))

    print("Least Square Parameters")
    print("a: " + str(a) + "\t b: " + str(b)) 

    print("Uncertainities")
    print("standard dev a: " + str(std_dev_a) + "\t standard dev b: " +str(std_dev_b))
    
    # Plot values
    Y = a + b*x
    plt.scatter(x, y, color='r', label='Dataset')
    plt.plot(x,Y, color='g', label='Regression Line')
    plt.legend()
    plt.show()

except Exception as e:
    print(e)
    logging.exception(e)

