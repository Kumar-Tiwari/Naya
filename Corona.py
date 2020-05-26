import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel('covid.xlsx',index=False)
for i in range(266):
    plt.plot(df.loc[i])
    plt.show()
