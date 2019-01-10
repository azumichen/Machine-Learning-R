# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:04:22 2018

@author: Anna Chen
"""


#探索性数据分析
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
df=pd.read_csv(r'...\web data.csv',engine='python')


df.head()
df.dtypes
df.describe()
df.info()

import seaborn as sns


#1.	找到article type 与page view之间的关系
sns.boxplot(x='Article type',y='Page views',data=df)


#2.	Num words 与page view 之间有什么关系
plt.scatter(x='Num words',y='Page views',data=df)

df2=df.copy()
df2['Num words_bin']=df2['Num words'].transform( lambda x: pd.qcut(x, 5, labels=list(range(1,6))))
sns.boxplot(x='Num words_bin',y='Page views',data=df2)



#3.	Num locations 与page view 之间的关系
plt.scatter(x='Num locations',y='Page views',data=df)
sns.boxplot(x='Num locations',y='Page views',data=df)

df.groupby('Num locations')['Page views'].count().reset_index(name='cnt')

sns.countplot(x='Num locations',data=df)




#breast_cancer
from random import shuffle  # 导入随机函数 shuffle，用来打乱数据
import seaborn as sns
from random import seed
import pandas as pd
######## load data
filename = r'...\breast_cancer.csv'
data = pd.read_csv(filename, engine='python')
data.head()
data.shape
data.describe()
data.info()

###  deal with missing values
data.fillna(data.mean(),inplace=True)

data.columns
##############  remove outliers
data_des=data.describe()

sns.boxplot(y="area error", data=data)

data = data[-(data['area error'] > 500)]



########################## split to train and test
data = data.as_matrix() # 将表格转换为矩阵
seed(123)
shuffle(data) # 随机打乱数据
p = 0.7 # 设置训练数据比例
train = data[:int(len(data)*p),:] # 前 70% 为训练集
test = data[int(len(data)*p):,:] # 后 30% 为测试集
x_train=train[:,1:]
y_train=train[:,0]
x_test=test[:,1:]
y_test=test[:,0]


######## logistic regression
from sklearn.linear_model import LogisticRegression as LR
lr = LR() # 建立逻辑回归模型
lr.fit(x_train, y_train) # 用筛选后的特征数据来训练模型
scores=lr.score(x_test, y_test)

pd.crosstab(y_test, lr.predict(x_test), rownames=['actual'], colnames=['preds'])


######## logistic ROC
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve,auc # 导入 ROC 曲线函数
predict_result = lr.predict_proba(x_test) # 预测结果
fpr, tpr, thresholds = roc_curve(y_test, predict_result[:, 1], pos_label=1)
roc_auc = auc(fpr, tpr)
plt.title('Logistic Regression ROC')
plt.plot(fpr, tpr, linewidth=2, label = 'AUC = %0.4f' % roc_auc) # 作出 ROC 曲线
plt.xlabel('False Positive Rate') # 坐标轴标签
plt.ylabel('True Positive Rate') # 坐标轴标签
plt.ylim(0,1.05) # 边界范围
plt.xlim(0,1.05) # 边界范围
plt.legend(loc=4) # 图例位置右下方
plt.plot([0, 1], [0, 1], 'r--')
plt.show() # 显示作图结果


#系数
lr.coef_ 

#截距
lr.intercept_ 


######## decision tree
from sklearn.tree import DecisionTreeClassifier # 导入决策树模型

dt = DecisionTreeClassifier() # 建立决策树模型
dt.fit(x_train,y_train) # 训练

dt.score(x_test, y_test)
pd.crosstab(y_test, dt.predict(x_test), rownames=['actual'], colnames=['preds'])




predict_result = dt.predict_proba(x_test) # 预测结果
fpr, tpr, thresholds = roc_curve(y_test, predict_result[:, 1], pos_label=1)
roc_auc = auc(fpr, tpr)
plt.title('Decision Tree ROC')
plt.plot(fpr, tpr, linewidth=2, label = 'AUC = %0.4f' % roc_auc) # 作出 ROC 曲线
plt.xlabel('False Positive Rate') # 坐标轴标签
plt.ylabel('True Positive Rate') # 坐标轴标签
plt.ylim(0,1.05) # 边界范围
plt.xlim(0,1.05) # 边界范围
plt.legend(loc=4) # 图例位置右下方
plt.plot([0, 1], [0, 1], 'r--')
plt.show() # 显示作图结果


#特征的重要性
print((dt.feature_importances_))

plt.bar(list(range(len(dt.feature_importances_))), dt.feature_importances_)



#绘制决策树图形
#第一步是安装graphviz。下载地址在：http://www.graphviz.org/。
#无论是linux还是windows，装完后都要设置环境变量,将graphviz的bin目录加到PATH，比如是windows，将C:/Program Files (x86)/Graphviz2.38/bin/加入PATH。
#import os
#os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
#
#第二步是安装python插件graphviz和插件pydotplus。
#通过pip 
   
import pydotplus
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
from sklearn import tree

dot_data = tree.export_graphviz(dt, out_file=None)   
graph = pydotplus.graph_from_dot_data(dot_data)   
graph.write_png(r"...\out.png")  #生成out.png
graph.write_pdf(r"...\out.pdf")  #生成out.pdf



###### Random Forest
from sklearn.ensemble import RandomForestClassifier
RF = RandomForestClassifier(n_jobs=-1)
RF.fit(x_train, y_train)

RF.score(x_test, y_test)
pd.crosstab(y_test, RF.predict(x_test), rownames=['actual'], colnames=['preds'])


predict_result = RF.predict_proba(x_test) # 预测结果
fpr, tpr, thresholds = roc_curve(y_test, predict_result[:, 1], pos_label=1)
roc_auc = auc(fpr, tpr)
plt.title('Random Forest ROC')
plt.plot(fpr, tpr, linewidth=2, label = 'AUC = %0.4f' % roc_auc) # 作出 ROC 曲线
plt.xlabel('False Positive Rate') # 坐标轴标签
plt.ylabel('True Positive Rate') # 坐标轴标签
plt.ylim(0,1.05) # 边界范围
plt.xlim(0,1.05) # 边界范围
plt.legend(loc=4) # 图例位置右下方
plt.plot([0, 1], [0, 1], 'r--')
plt.show() # 显示作图结果    

plt.bar(list(range(len(RF.feature_importances_))), dt.feature_importances_)
