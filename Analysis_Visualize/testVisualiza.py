import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

import numpy as np
import pandas as pd
import seaborn as sns
plt.style.use('classic')
"""
x = [1,2,3]
y = [1,2,4]
plt.scatter(x,y)
plt.xlim(0,10)
plt.ylim(0,10)
#scatter plot color
plt.scatter(x,y, s = 10, c ='red', marker='*')
#add tilte
plt.title('Test Visualize')
plt.xlabel('X')
plt.ylabel('Y')
plt.show() """

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]],size=2000)
b =2