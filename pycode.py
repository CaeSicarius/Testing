##Sample code written in python3

import numpy as np
import pandas as pd


print('Can I udpate this code off GitHub?')

##Updating in Spyder Anaconda
print('Used Git to Clone Repo Testing to laptop')
print('Updating using Spyder3')

x = np.linspace(0,1,50,dtype='float')
y = 2*x
def square(x):
    return np.power(x,x)

z = square(y)
data = np.hstack([x,y,z]).reshape(3,50)
print(data.shape)

test_df = pd.DataFrame(data=data.T)
print(test_df)
test_df.plot()
## End Updated Code Here