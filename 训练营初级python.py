# -*- coding: utf-8 -*-
import os

#修改成文件所在路径
d=r'C:\训练营初级数据和代码'
os.chdir(d)


#==============================================================================
# python保留字
#==============================================================================
import keyword
keyword.kwlist


#==============================================================================
# 注释
#==============================================================================
# 第一个注释
# 第二个注释
 
'''
第三注释
第四注释
'''
 
"""
第五注释
第六注释
"""
print ("Hello, Python!")


#==============================================================================
# 行和缩进
#==============================================================================
if True:
    print ("True")
else:
    print ("False")
    
#以下代码将会执行错误：
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
  print ("False")    # 缩进不一致，会导致运行错误
  

#==============================================================================
# 多行语句

#==============================================================================
#但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
total = item_one + \
        item_two + \
        item_three

#语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

#==============================================================================
# 数值运算

#==============================================================================
5 + 4  # 加法
 4.3 - 2 # 减法
 3 * 7  # 乘法
 2 / 4  # 除法，得到一个浮点数
 2 // 4 # 除法，得到一个整数
 17 % 3 # 取余 
 2 ** 5 # 乘方


#==============================================================================
#  字符串(String)
#==============================================================================
str = 'python'
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次
print (str + "TEST") # 连接字符串

print('Ru\noob')
print(r'Ru\noob')

word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])

#==============================================================================
# List（列表）
#==============================================================================
list1 = [ 'abcd', 786 , 2.23, 'python', 70.2 ]
tinylist = [123, 'python']
print (list1)            # 输出完整列表
print (list1[0])         # 输出列表第一个元素
print (list1[:])       # 从第二个开始输出到第三个元素
print (list1[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list1 + tinylist) # 连接列表
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
a
a[2:5] = []   # 将对应的元素值设置为 [] 
a

#==============================================================================
# 元组- tuple

#==============================================================================
tuple1 = ( 'abcd', 786 , 2.23, 'Python', 70.2  )
tinytuple = (123, 'Python')
 
print (tuple1)             # 输出完整元组
print (tuple1[0])          # 输出元组的第一个元素
print (tuple1[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple1[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple1 + tinytuple) # 连接元组

tup = (1, 2, 3, 4, 5, 6)
print(tup[0])

print(tup[1:5])

tup[0] = 11  # 修改元组元素的操作是非法的

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

#==============================================================================
# 集合- set

#==============================================================================
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'} 
print(student)   # 输出集合，重复的元素被自动去掉 
# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中') 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam') 
print(a) 
print(a - b)     # a和b的差集 
print(a | b)     # a和b的并集 
print(a & b)     # a和b的交集 
print(a ^ b)     # a和b中不同时存在的元素

#==============================================================================
# 字典- dict
#==============================================================================
dict1 = {}
dict1['one'] = '1 – 机器学习'
dict1[2]     = "2 - python"
 
tinydict = {'name': 'python','code':1, 'site': 'www.python.com'}
 
 
print (dict1['one'])       # 输出键为 'one' 的值
print (dict1[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

dict([('Python', 1), ('Google', 2), ('Taobao', 3)])
 
 {x: x**2 for x in (2, 4, 6)}
 
 dict(Python=1, Google=2, Taobao=3)
 
 
#==============================================================================
# while 循环 
#==============================================================================
condition = 0
while condition < 10:
    print(condition)
    condition = condition + 1
 
 
#==============================================================================
# for 循环
#==============================================================================
example_list = [1,2,3,4,5,6,7,12,543,876,12,3,2,5]
for i in example_list:
    print(i)


#==============================================================================
# range使用

#==============================================================================
for i in range(1, 10):
    print(i)

for i in range(0,13, 5):
    print(i)

#==============================================================================
# if 判断

#==============================================================================
x = 1
y = 2
z = 3
if x < y:
    print('x is less than y')

if x < y < z:
    print('x is less than y, and y is less than z')


x = 1
y = 2
z = 3
if x = y:
    print('x is equal to y')

x = 2
y = 2
z = 0
if x == y:
    print('x is equal to y')

#==============================================================================
# Python数据读写
#==============================================================================
import pandas as pd

#读取csv文件
df=pd.read_csv('housing.csv',engine='python') 
df.head() #查看数据前5行

#读取txt文件
df=pd.read_table('housing.txt',engine='python',sep=',') 
df.head() #查看数据前5行
df.to_csv(r'housing.csv')


# pip install pymysql
import pymysql ##加载pymysql.cursors模块
# Connect to the database
connection = pymysql.connect(host='47.97.12.198', ##host 47.97.12.198
port=3306, ##默认端口 3306
user='student', ##默认用户名 SHstu
password='student123', ##密码 123456
db='student', ##已有database student
charset='utf8mb4', ##编码库，默认utf8
)

data=pd.read_sql_query("SELECT * FROM offices",con=connection) ##直接用read_sql_query直接执行数据语言
data.head()
connection.close()


dat =pd.read_table('http://www.stats.ox.ac.uk/pub/datasets/csb/ch11b.dat')
dat.head()

# pip install tushare
import tushare as ts
from matplotlib import pyplot as plt

data=ts.get_k_data(code='002337',ktype='D') #一次性获取全部日k线数据
data.head()
plt.plot(data.close)

#==============================================================================
# Numpy包的介绍

#==============================================================================
import numpy as np #为了方便使用numpy 采用np简写

array = np.array([[1,2,3],[2,3,4]])  #列表转化为矩阵
print(array)
print('number of dim:',array.ndim)  # 维度
print('shape :',array.shape)    # 行数和列数
print('size:',array.size)   # 元素个数

#创建数组 
a = np.array([2,23,4])  # list 1d
print(a)
# [2 23 4]
#指定数据 dtype 
a = np.array([2,23,4],dtype=np.int)
print(a.dtype)
# int 64
a = np.array([2,23,4],dtype=np.int32)
print(a.dtype)
# int32
a = np.array([2,23,4],dtype=np.float)
print(a.dtype)

# float64
a = np.array([2,23,4],dtype=np.float32)
print(a.dtype)
# float32

#创建特定数据 
a = np.array([[2,23,4],[2,32,4]])  # 2d 矩阵 2行3列
print(a)

#创建全零数组
a = np.zeros((3,4)) # 数据全为0，3行4列

#创建全一数组, 同时也能指定这些特定数据的 dtype:
a = np.ones((3,4),dtype = np.int)   # 数据为1，3行4列

#创建全空数组, 其实每个值都是接近于零的数:
a = np.empty((3,4)) # 数据为empty，3行4列

#用 arange 创建连续数组:
a = np.arange(10,20,2) # 10-19 的数据，2步长

#使用 reshape 改变数据的形状
a = np.arange(12).reshape((3,4))    # 3行4列，0到11

#用 linspace 创建线段型数据:
a = np.linspace(1,10,20)    # 开始端1，结束端10，且分割成20个数据，生成线段



import numpy as np
a=np.array([10,20,30,40])   # array([10, 20, 30, 40])
b=np.arange(4)              # array([0, 1, 2, 3])

c=a-b  # array([10, 19, 28, 37])
c=a+b   # array([10, 21, 32, 43])
c=a*b   # array([  0,  20,  60, 120])
c=b**2  # array([0, 1, 4, 9])

c=10*np.sin(a)  
print(b<3)  

import numpy as np
A = np.arange(3,15)
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
         
print(A[3])    # 6

A = np.arange(3,15).reshape((3,4))
print(A[2])   
print(A[1][1])      # 8
print(A[1, 1])      # 8
print(A[1, 1:3])    # [8 9]

for row in A:
    print(row)
   
for column in A.T:
    print(column)

import numpy as np
A = np.arange(3,15).reshape((3,4))
         
print(A.flatten())   
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

for item in A.flat:
    print(item)


#==============================================================================
# Pandas包的介绍
#==============================================================================
import pandas as pd
import numpy as np


s = pd.Series([1,3,6,5,44,1])

print(s)

#通过列表创建
pd.Series([4, 7, -5, 3])
#通过元组创建
pd.Series((4, 7, -5, 3), index=['d', 'b', 'a', 'c'])
#通过字典创建
sdata = { 'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000 }
pd.Series(sdata)


pd.DataFrame({'a':[1,2,3],'b':[4,5,6]})
df = pd.DataFrame(np.arange(16).reshape(4,4),columns=['a','b','c','d'])
print(df)

#通过字典创建
pd.DataFrame({'a':[1,2],'b':[2,3],'c':[3,4],'d':[4,5]})
#通过数组创建
pd.DataFrame(np.array([[1,2,3,4],[3,4,5,6]]),index=['one','two'])
#通过Series创建
data=pd.DataFrame([pd.Series([11,12,13,14]), pd.Series([21,22,23,24])])
#通过其他DataFrame创建
pd.DataFrame(data,index=[0,1,'one'],columns=[0,1,2,'a'])


#查看数据
df.columns
df.index
df.values
df.dtypes
df.shape

df.head()
df.tail()
df.describe()

#选取数据
df[0:2]
type(df['a'])
type(df[['a','b']])
df.loc[:,'a']
df.iloc[0,0]
df[df['a']>0]

#赋值
df.iloc[0,0]=100
df['b']=99
df.loc[df['c']==10,'d']=88
df['e']=99


#计算
df['a']+df['b']
df['d']=df['a']+df['b']


#Pandas-缺失值处理

#建立了一个6X4的矩阵数据并且把两个位置置为空.
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

df.dropna() 
#如果想直接去掉有 NaN 的行或列, 可以使用 dropna

df.dropna(
    axis=0,     # 0: 对行进行操作; 1: 对列进行操作
    how='any'   # 'any': 只要存在 NaN 就 drop 掉; 'all': 必须全部是 NaN 才 drop 
    ) 


df.fillna(value=0)

df.isnull() 
    
np.any(df.isnull()) == True 


#定义资料集
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
#concat纵向合并
res = pd.concat([df1, df2, df3], axis=0)

#ignore_index (重置 index)
#承上一个例子，并将index_ignore设定为True
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)

#打印结果
print(res)


#定义资料集并打印出
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})
    
#依据key column合并，并打印出
res = pd.merge(left, right, on='key')

print(res)


#定义资料集并打印出
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})

#依据key1与key2 columns进行合并，并打印出四种结果['left', 'right', 'outer', 'inner']
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
print(res)


res = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print(res)


res = pd.merge(left, right, on=['key1', 'key2'], how='left')
print(res)

res = pd.merge(left, right, on=['key1', 'key2'], how='right')
print(res)


df = pd.DataFrame({
            'key1':     ['a', 'a', 'b', 'b', 'a'],
            'key2':     ['one', 'two', 'one', 'two', 'one'],
            'data1':    np.random.randn(5),
            'data2':    np.random.randn(5)
        }) 
# 按key1分组, 计算data1列的平均值
key1 = df.groupby('key1', as_index=False)['data1'].mean()
type(df.groupby('key1')['data1'].mean())

# 按照key1, key2分组, 对data1列计数
key12 = df.groupby(['key1', 'key2'], as_index=False)['data1'].count()


#agg数据聚合
key1 = df.groupby('key1', as_index=False)['data1'].agg({'aa' : 'count'})


#query
from numpy.random import randn
df = pd.DataFrame(randn(10, 2), columns=list('ab')) #randn 返回标准正态分布的数组
df.query('a > b')
df[df.a > df.b]  # same result as the previous expression


#eval
df = pd.DataFrame({'A': range(1, 6), 'B': range(10, 0, -2)})
df.eval('C = A + B',in)
df.eval('C = A + B', inplace=True) # inplace 是否在原来的数据上修改
df
df.eval('''
        D = A-B
        F = A*B
        ''')

#drop
df = pd.DataFrame(np.arange(12).reshape(3,4),
                 columns=['A', 'B', 'C', 'D'])
df

#Drop columns
df.drop(['B', 'C'], axis=1)
df.drop(columns=['B', 'C'])

#Drop a row by index
df.drop([0, 1])



#rename
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
df
df.rename(index=str, columns={"A": "a", "B": "c"})

         
#==============================================================================
# Python 作图
#==============================================================================
#在console中输出图片
%matplotlib inline 

#在单独窗口中输出图片
%matplotlib qt5 



import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2*x + 1

plt.figure()
plt.plot(x, y)
plt.title('fig1')
plt.show()


x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')
plt.show()


# set line syles
l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')
plt.legend(loc='upper right')
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')


#seaborn
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

diamonds=pd.read_csv('diamonds.csv',engine='python')
diamonds.head()
diamonds.shape
ds=diamonds.sample(frac=0.1) #随机抽取10%的数据
ds.shape

#scatter
plt.scatter(ds.carat,ds.price)

plt.scatter(np.log(ds.carat),np.log(ds.price)) 


#FacetGrid
g = sns.FacetGrid(ds, hue='color', size=7.5)
g.map(plt.scatter, 'carat', 'price').add_legend()

#boxplot
sns.boxplot(x="color", y="price", data=ds) 

#countplot
sns.countplot(x='color',data=ds)

#hist
sns.distplot(ds.carat, kde=False)
sns.distplot(ds.carat, kde=True)

#facet
g=sns.FacetGrid(data=ds,col='color',col_wrap=3)   # 这里相当于groupby
g=g.map(sns.distplot,'carat')
    
    
#饼图
# The slices will be ordered and plotted counter-clockwise.
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs' # 定义标签
sizes = [15, 30, 45, 10] # 每一块的比例
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'] # 每一块的颜色
explode = (0, 0.1, 0, 0) # 突出显示，这里仅仅突出显示第二块（即 'Hogs' ）
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
shadow=True, startangle=90)
plt.axis('equal') # 显示为圆（避免比例压缩为椭圆）
plt.show()


#热力图
flights = sns.load_dataset('flights')
flights.head()

# pivot() 可以将dataframe转换为行列式矩阵 并指定每个元素的存储值
flights = flights.pivot(index='month', columns='year',  values='passengers')
# print(flights)

plt.figure(figsize=(10,6))
sns.heatmap(flights, fmt='d', linewidths=.5)
# fmt设置字体模式  linewidth设置每个小方格的间距 线宽




#==============================================================================
# 爬虫
#==============================================================================
import requests
from lxml import etree

#我们邀抓取的页面链接
url='https://book.douban.com/subject/1084336/comments/'

#用requests库的get方法下载网页
r=requests.get(url).text

#解析网页并且定位短评
s=etree.HTML(r)
file=s.xpath('//*[@id="comments"]/ul/li/div[2]/p/span/text()')

#//*[@id="comments"]/ul/li[1]/div[2]/p/span
#//*[@id="comments"]/ul/li[2]/div[2]/p/span
#打印抓取的信息
print(file)
    
def get_content(url):
    r=requests.get(url).text   
     
    #解析网页并且定位短评
    s=etree.HTML(r)
    file=s.xpath('//*[@id="comments"]/ul/li/div[2]/p/span/text()')
    
    return file

file='douban.txt'

for i in range(1,5):
    url="http://book.douban.com/subject/1084336/comments/hot?p={}".format(i)
    file=get_content(url)
    with open(file,'a+',encoding='utf-8') as f:
        for line in file:
            f.write(line+'\n')    
    
#pip install wordcloud jieba
            
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import jieba
from imageio import imread
import numpy as np

with open(file,encoding='utf-8') as f:
    text=f.read() 


#词云制作
    
wordlist_after_jieba = jieba.cut(text, cut_all = False)
wl_space_split = " ".join(wordlist_after_jieba)

font_path=r'C:\Windows\Fonts\SimHei.ttf'
back_coloring_path = 'xiaowangzi.png' # 设置背景图片路径

back_coloring = imread(back_coloring_path)# 设置背景图片

wc = WordCloud(font_path=font_path,  # 设置字体
               background_color="white",  # 背景颜色
               max_words=2000,  # 词云显示的最大词数
               mask=back_coloring,  # 设置背景图片
               max_font_size=100,  # 字体最大值
               random_state=42,
               width=1000, height=860, margin=2,# 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
               )

wc.generate(wl_space_split)


# 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
plt.figure(figsize=(24,18))
plt.imshow(wc)
plt.axis("off")
plt.show()
# 绘制词云

# 绘制以背景图片为颜色的图片
# 我们还可以直接在构造函数中直接给颜色
# 通过这种方式词云将会按照给定的图片颜色布局生成字体颜色策略
plt.figure(figsize=(24,18))
image_colors = ImageColorGenerator(back_coloring)
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.show()

imgname='output.jpg'
# 保存图片
wc.to_file(imgname)    
    

#==============================================================================
# credit score
#==============================================================================
from random import shuffle  # 导入随机函数 shuffle，用来打乱数据
import seaborn as sns
from random import seed
import pandas as pd
######## load data
filename = 'cs-data.csv'
data = pd.read_csv(filename, engine='python')
data.head()
data.shape
data.describe()

###  deal with missing values
data.fillna(data.mean(),inplace=True)
data.describe()

data.columns
##############  remove outliers

data.plot(kind='box', subplots=True, layout=(4,4),sharex=False, sharey=False, fontsize=8,figsize=(24,18))


sns.boxplot(y="age", data=data)
data = data[-(data['age'] > 100)]

sns.boxplot(y="NumberOfTime30-59DaysPastDueNotWorse", data=data)
data = data[-(data['NumberOfTime30-59DaysPastDueNotWorse'] > 80)]
sns.boxplot(y="NumberOfTime30-59DaysPastDueNotWorse", data=data)

sns.boxplot(y="NumberOfOpenCreditLinesAndLoans", data=data)

sns.boxplot(y="DebtRatio", data=data)
data = data[-(data['DebtRatio'] > 100000)]
sns.boxplot(y="DebtRatio", data=data)

sns.boxplot(y="MonthlyIncome", data=data)
data = data[-(data['MonthlyIncome'] > 500000)]
sns.boxplot(y="MonthlyIncome", data=data)


data.hist(xlabelsize=7,ylabelsize=7,figsize=(16,12))


# 正负样本比例

grouped=data[['SeriousDlqin2yrs']].groupby('SeriousDlqin2yrs')['SeriousDlqin2yrs'].count()

grouped.plot(kind='bar')

grouped=grouped.reset_index(name='cnt')

grouped['percent']=grouped['cnt']/grouped['cnt'].sum()

grouped


#再看年龄对违约客户率的影响，违约客户率随着年龄增大而逐步下降

df1=data.groupby('age')['age'].count().reset_index(name='cnt_total')

df2=data.query('SeriousDlqin2yrs==1').groupby('age')['age'].count().reset_index(name='cnt_Dlq')

df3=pd.merge(df1,df2,how='left',on='age').fillna(0).eval('percent_Dlq=cnt_Dlq/cnt_total')

df3.plot(x='age',y='percent_Dlq')


# 相关系数热力图
corr=data.corr()

plt.subplots(figsize=(24, 24)) # 设置画面大小
sns.heatmap(corr, annot=True, vmax=1, square=True, cmap="Blues")

plt.show()


# 各变量与目标变量的相关性
s=corr['SeriousDlqin2yrs']
s=s[s.index!='SeriousDlqin2yrs']

plt.figure(figsize=(24,18))
plt.barh(range(len(s)), s, tick_label = s.index)
plt.show()


# 按照7：3的比例随机分割数据
from sklearn.model_selection import train_test_split

x=data.iloc[:,1:]
y=data.iloc[:,0]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=2018)



######## logistic regression
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
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
plt.plot(fpr, tpr, linewidth=2, label = 'AUC = %0.2f' % roc_auc) # 作出 ROC 曲线
plt.xlabel('False Positive Rate') # 坐标轴标签
plt.ylabel('True Positive Rate') # 坐标轴标签
plt.ylim(0,1.05) # 边界范围
plt.xlim(0,1.05) # 边界范围
plt.legend(loc=4) # 图例位置右下方
plt.plot([0, 1], [0, 1], 'r--')
plt.show() # 显示作图结果



######## decision tree
from sklearn.tree import DecisionTreeClassifier # 导入决策树模型
tree = DecisionTreeClassifier() # 建立决策树模型
tree.fit(x_train,y_train) # 训练

tree.score(x_test, y_test)
pd.crosstab(y_test, tree.predict(x_test), rownames=['actual'], colnames=['preds'])

predict_result = tree.predict_proba(x_test) # 预测结果
fpr, tpr, thresholds = roc_curve(y_test, predict_result[:, 1], pos_label=1)
roc_auc = auc(fpr, tpr)
plt.title('Decision Tree ROC')
plt.plot(fpr, tpr, linewidth=2, label = 'AUC = %0.2f' % roc_auc) # 作出 ROC 曲线
plt.xlabel('False Positive Rate') # 坐标轴标签
plt.ylabel('True Positive Rate') # 坐标轴标签
plt.ylim(0,1.05) # 边界范围
plt.xlim(0,1.05) # 边界范围
plt.legend(loc=4) # 图例位置右下方
plt.plot([0, 1], [0, 1], 'r--')
plt.show() # 显示作图结果

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
plt.plot(fpr, tpr, linewidth=2, label = 'AUC = %0.2f' % roc_auc) # 作出 ROC 曲线
plt.xlabel('False Positive Rate') # 坐标轴标签
plt.ylabel('True Positive Rate') # 坐标轴标签
plt.ylim(0,1.05) # 边界范围
plt.xlim(0,1.05) # 边界范围
plt.legend(loc=4) # 图例位置右下方
plt.plot([0, 1], [0, 1], 'r--')
plt.show() # 显示作图结果    

