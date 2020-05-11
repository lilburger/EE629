# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('nba_players_with_salary.csv')
head = data.head()
print head
describe = data.describe()
print describe
dat_cor=data.loc[:,['RPM','AGE','SALARY_MILLIONS','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','POINTS','GP','MPG','ORPM','DRPM']]
coor=dat_cor.corr()
sns.heatmap(coor,square=True, linewidths=0.02, annot=False) 
#Heatmap function in seaborn is a heatmap function that intersects multidimensional value variables according to their value size.
#Top 10 highest-paid players
data_money = data.loc[:,['PLAYER','SALARY_MILLIONS','RPM','AGE','MPG']].sort_values(by='SALARY_MILLIONS',ascending=False).head(10)
print data_money
#Top 10 highest-effienicy players
data_effiency = data.loc[:,['PLAYER','RPM','SALARY_MILLIONS','AGE','MPG']].sort_values(by='RPM',ascending=False).head(10)
print data_effiency
#Top 10 highest-time players
data_time = data.loc[:,['PLAYER','RPM','SALARY_MILLIONS','AGE','MPG']].sort_values(by='MPG',ascending=False).head(10)
print data_time
sns.set_style('darkgrid') #Set seaborn's panel style
plt.figure(figsize=(12,12))
plt.subplot(3,1,1)  #Split the page, multi-figure display
sns.distplot(data['SALARY_MILLIONS'])
plt.xticks(np.linspace(0,40,9))
plt.ylabel(u'$Salary$',size=10)

plt.subplot(3,1,2)
sns.distplot(data['RPM'])
plt.xticks(np.linspace(-10,10,9))
plt.ylabel(u'$RPM$',size=10)

plt.subplot(3,1,3)  
sns.distplot(data['AGE'])
plt.xticks(np.linspace(20,40,11))
plt.ylabel(u'$AGE$',size=10)
dat1=data.loc[:,['RPM','SALARY_MILLIONS','AGE','POINTS']]
sns.jointplot(dat1.SALARY_MILLIONS,dat1.AGE,kind='kde',size=8) 
dat1=data.loc[:,['RPM','SALARY_MILLIONS','AGE','POINTS']]
sns.pairplot(dat1) #Correlation display, diagonal distribution display, can intuitively see whether the variable has a current relationship

data['avg_point']=data['POINTS']/data['MP'] #Point per minutes
def age_cut(df):
    if df.AGE<=24:
        return 'young'
    elif df.AGE>=30:
        return 'old'
    else:
        return 'best'
data['age_cut']=data.apply(lambda x: age_cut(x),axis=1) #Players is in the best age or not
data['cnt']=1 #Count 

### Players' salary and efficiency are measured by age
sns.set_style('darkgrid') #Set seaborn's panel style
plt.figure(figsize=(8,8))
plt.title(u'$RPM\ and\ SALARY$',size=15)
X1=data.loc[data.age_cut=='old'].SALARY_MILLIONS
Y1=data.loc[data.age_cut=='old'].RPM
X2=data.loc[data.age_cut=='best'].SALARY_MILLIONS
Y2=data.loc[data.age_cut=='best'].RPM
X3=data.loc[data.age_cut=='young'].SALARY_MILLIONS
Y3=data.loc[data.age_cut=='young'].RPM
plt.plot(X1,Y1,'.')
plt.plot(X2,Y2,'.')
plt.plot(X3,Y3,'.')
plt.xlim(0,30)
plt.ylim(-8,8)
plt.xlabel('Salary',size=10)
plt.ylabel('RPM',size=10)
plt.xticks(np.arange(0,30,3))
plt.legend(['old','best','young'])
dat2=data.loc[:,['RPM','POINTS','TRB','AST','STL','BLK','age_cut']]
sns.pairplot(dat2,hue='age_cut')
plt.show()
### Operate in groups by team
dat_grp=data.groupby(by=['TEAM'],as_index=False).agg({'SALARY_MILLIONS':np.mean,'RPM':np.mean,'PLAYER':np.size})
dat_grp=dat_grp.loc[dat_grp.PLAYER>5]  #Players not considered for transfer during the season
grp=dat_grp.sort_values(by='SALARY_MILLIONS',ascending=False).head(10)
print grp
### Operate in groups by position
dat_grp2=data.groupby(by=['TEAM','age_cut'],as_index=False).agg({'SALARY_MILLIONS':np.mean,'RPM':np.mean,'PLAYER':np.size})
dat_grp2=dat_grp2.loc[dat_grp2.PLAYER>3]     ##Delete those uncertain poisition player
graph2=dat_grp2.sort_values(by=['PLAYER','RPM'],ascending=False).head(15)
print graph2
##Visualization by team data
dat_grp3=data.groupby(by=['TEAM'],as_index=False).agg({'SALARY_MILLIONS':np.mean,'RPM':np.mean,'PLAYER':np.size,'POINTS':np.mean,'eFG%':np.mean,'MPG':np.mean,'AGE':np.mean})
dat_grp3=dat_grp3.loc[dat_grp3.PLAYER>5]
graph3=dat_grp3.sort_values(by=['RPM'],ascending=False).head(10)
print graph3