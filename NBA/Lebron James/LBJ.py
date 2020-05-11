# -*- coding: utf-8 -*-
"""
Created on Mon May 11 08:17:13 2020

@author: Chen Junyan
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('LBJ.csv')
print data.shape
print data.describe

total_points=(data.PTS*data.G).sum()
avg_points=total_points/data.G.sum()
print u'Regular season Total points: ',total_points
print u'Regular season average points: ',avg_points

max_point=data.PTS.max()
print(data[data.PTS==max_point])
print(data.loc[data.PTS>=30])

max_data={'point':data.PTS.max(),
          'rebounds':data.TRB.max(),
          'assistants':data.AST.max(),
          'steals':data.STL.max(),
          'blocks':data.BLK.max()}

best_LBJ=pd.Series(max_data)
print best_LBJ

x=pd.date_range('2003','2019',freq='365D')
y=data.PTS
plt.xlabel('season')
plt.ylabel('points')
plt.plot(x,y)
plt.show()

x=pd.date_range('2003','2019',freq='365D')
y=data.TRB
plt.xlabel('season')
plt.ylabel('rebounds')
plt.plot(x,y)
plt.show()

x=np.array([x for x in range(2003,2020)])
y=data.AST
plt.xlabel('season')
plt.ylabel('points')
plt.bar(x,y,width=0.5,color='m')
plt.xticks(x)
ax=plt.gca()
plt.show()