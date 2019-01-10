

################################################################
#                                                              #
#                                                              #
#  机器学习R语言部分                                  #
#                                                              #
################################################################


#install.packages("ggplot2")

library(ggplot2)

### R语言的数据类型
## 数字型
x<-1
x=1
x

class(x)

y=1/0
class(y)

z=0/0
class(z)

##字符型
x="A"
x
y="R语言"
y
class(x)
class(y)

z="1"
class(z)

##逻辑型
x=TRUE
x
class(x)

x=5
#对x的值进行判断

x==6

x<4

x>=2

## 向量型

x=c(1,2,3,4,5,6)

x

y=c("a","b","c","d")
y

## 列表

ll =  list(1,"a",FALSE,c(1,2,3))

## 矩阵
m = matrix(1:6, nrow = 2, ncol = 3,byrow=T)
m

## 数据类型之间的转换
x = 0:6
x="1"
10*x
xx = as.numeric(x)
10*xx
class(as.character(x))

as.logical(x)


#####  第二部分：R语言数据读写

###手动输入
scores <- c(61, 66, 90, 88, 100)


points <- data.frame(
  label=c("Low", "Mid", "High"),
  lbound=c( 0, 0.67, 1.64),
  ubound=c(0.674, 1.64, 2.33)
)


#导入本地数据

#getwd()

setwd("C:/CPDA/机器学习课程2018/data/")

WIN: loan_dat = read.csv("C:\\R work\\input data\\信用评分.csv",header=T,sep=",")
MAC: data <- read.csv("~/Desktop/Dataset/168 PreWeek1.csv",header = TRUE)

loan_dat = read.table("信用评分.txt",header=T)

head(loan_dat)

dim(loan_dat)

###导入互联网数据
dat =read.table('http://www.stats.ox.ac.uk/pub/datasets/csb/ch11b.dat')
head(dat)

###通过R包读取专业数据
#install.packages("quantmod")
library(quantmod)
getSymbols("BABA")
chartSeries(BABA, subset='last 6 months')
addBBands()

### 链接Mysql数据库
#install.packages("RMySQL")
library(RMySQL)
library(DBI)
#options(digits=5)
con <- dbConnect(MySQL(),host="47.97.12.198",dbname="student",user="SHstu",password="123456")

#解决中文乱码问题
#dbSendQuery(con,'SET NAMES uft8')
res <- dbSendQuery(con, "SELECT * FROM offices")  
offices  <- dbFetch(res)
#断开连接
dbDisconnect(con)


###数据写到本地

write.table(loan_dat,"C:\\R work\\input data\\信用数据output.txt",row.names = F)



############## 第三部分：R语言的基本运算 ###################

x = c(1, 2, 3, 4)
class(x)
length(x)

y = list(17, "A nice day", TRUE)
class(y)
length(y)



list(c(15, 16, 17), "A nice day", TRUE)



c(a = 1, b = 2, c = 3)

list(a = 1:4, b = "string")


x = c(a = 1, b = 2, 3)
names(x)

names(x) = c("A", "B", "C")
x

x = c(10, 20, 30, 40, 50)

x[1]
x[5]
x[6]

x[c(1,5,6)]

x = c(10, 20, 30, 40, 50)
x[-c(1,2,3)]


x = c(10, 20, 30, 40)
x[c(FALSE, TRUE, FALSE, TRUE)]


x = c(10, 20, 30, 40)
x[c(FALSE, TRUE)]



x = c(a = 1, b = 2, c = 3)
x

x[c("a","b")]

##alter 

x = c(10, 20, 30, 40, 50)

x[1] = 11

x

x[x > 20] = c(100, 200)
x



##vector calculation
c(1, 2, 3) / c(0.1, 0.2, 0.3)

c(1, 2, 3) + 10
c(1, 2, 3) * 10



c(1, 2, 3, 4) * c(1, 2)

# summary function

max(1:100)
max(1:100, Inf)
range(1:100)
sum(1:100)
prod(1:10)

options(digits=5)

seq(0, 1, by = 0.1)

seq(0, 1, length=21)


rep(1:4, 3)

rep(1:4, c(2, 3, 2, 3))

rep(1:4, rep(3, 4))


# logical calculation

x = c(1, 2, 3, 4)

x < 2 & x != 3


all(x > 1)

any(x > 4)

## character

s = c("first", "second", "third")
s[1]

s[1] = "initial"
s
nchar(s)

substring(s, c(1,2,2), c(1,4,5))


paste("First", "Second", "Third")

paste("First", "Second", "Third", sep = ":")

paste("First", "Second", "Third", sep = "")

paste("element",s,"element",sep = "-")

###########define a function

square = function(x) { x * x }
square

square(10)

square(1:10)




x=-2
if (x > 0) y = sqrt(x) else y = -sqrt(-x)
y



x=1:10

s = 0

for(i in 1:length(x))
  s = s + x[i]
s


s = 0
for(val in x)
  s = s + val
s


################################################################
#                                                              #
#                                                              #
#  探索性数据分析                                 #
#                                                              #
################################################################


####################### R graphics
library(ggplot2)
dim(diamonds)

dsmall <- diamonds[sample(nrow(diamonds), 100), ]
dim(dsmall)

qplot(carat, price, data = diamonds)


qplot(log(carat), log(price), data = diamonds)


qplot(carat, price, data = diamonds, colour = cut)


qplot(carat, price, data = dsmall, shape = cut, colour = color)

#qplot(carat, price, data = diamonds, geom = c("point", "smooth"))

###

ggplot(BOD, aes(x=Time, y=demand)) + geom_line()

##boxplot
qplot(cut, price / carat, data = diamonds, geom = "boxplot")

## barplot

qplot(color, data = diamonds, geom = "bar")


## hist and density

qplot(carat, data = diamonds, geom = "histogram")

qplot(carat, data = diamonds, geom = "density") 


# time series

qplot(date, unemploy / pop, data = economics, geom = "line")


qplot(date, uempmed, data = economics, geom = "line") 


# facet

qplot(carat, data = diamonds, facets = color ~ cut,
      geom = "histogram", binwidth = 0.1, xlim = c(0, 3))


## other options

qplot(
  carat, price, data = dsmall,
  xlab = "Weight (carats) ", ylab = "Price ($)",
  main = "Price-weight relationship"
)


#####################################  EDA basic  ###############
#install.packages("dplyr")
library(dplyr)

setwd("C:\\R work\\input data\\")
flight = read.csv("flights.csv",header=T,sep=",")
head(flight)

## select 
aa=select(flight,year,month,day)
class(aa)

select(flight,year:day)

select(flight,-(year:day))


## distinct
distinct(flight,origin)
distinct(flight,dest)
distinct(flight,origin,dest)

## filter

filter(flight,month==1,day==2)

filter(flight,month==1|month==2)

## arrange
arrange(flight,dep_delay)

arrange(flight,month,desc(dep_delay))

## rename

rename(flight,tail_num=tailnum)

## mutate

mutate(flight,tot_delay=arr_delay+dep_delay)

mutate(flight,tot_delay=arr_delay+dep_delay,speed =distance/air_time*60 )

## summarise
summarise(flight,avg_dep_delay=mean(dep_delay,na.rm=T))

summarise(flight,avg_dep_delay=sd(dep_delay,na.rm=T))


by_origin = group_by(flight,origin)
delay = summarise(by_origin,
                  count=n(),
                  delay = mean(arr_delay,na.rm=T))

## sample_n
sample_n(flight,10)
sample_frac(flight,0.01)

## %>%



by_origin = group_by(flight,origin)
delay = summarise(by_origin,
                  count=n(),
                  delay = mean(arr_delay,na.rm=T))


group_by(flight,origin)%>% summarise(count=n(),delay = mean(arr_delay,na.rm=T))

# 3function
flight1=mutate(flight,tot_delay=arr_delay+dep_delay)
by_origin = group_by(flight1,origin)
summarise(by_origin,count=n(), delay = mean(tot_delay,na.rm=T))

mutate(flight,tot_delay=arr_delay+dep_delay)%>%group_by(origin)%>%summarise(count=n(), delay = mean(tot_delay,na.rm=T))


#### check your data #####

head(flight)

dim(flight)

str(flight)

summary(flight)

### check single variable

summary(flight$distance)
range(flight$distance)
quantile(flight$distance)
quantile(flight$distance,seq(0,1,by=0.1))
hist(flight$distance)
plot(density(flight$distance))


barplot(table(flight$origin))
pie(table(flight$origin))

### multiple variable analysis
cov(flight$arr_delay,flight$dep_delay, use="complete")
cor(flight$arr_delay,flight$dep_delay, use="complete")

cor(flight[4:7],use="complete")

boxplot(dep_delay~origin,data = flight)
boxplot(log(dep_delay)~origin,data = flight)
boxplot(log(dep_delay)~carrier,data = flight)



with(sample_n(flight,10000),plot(dep_delay,distance,col =origin))

pairs(flight[,4:7])



###  EDA case study #################

##1. loading data
housing = read.csv("C:\\CPDA\\R语言初级课程\\第二天\\第二天数据\\housing.csv",header=T,sep=",")
head(housing)
tail(housing)


##2. overall checking
str(housing)
dim(housing)
summary(housing)

##3. extreme value check


plot(housing$room)

housing[which(housing$room>60),]
housing=housing[-which(housing$room>60),]
plot(housing$room)
hist(housing$room)

## 4.answer questions
##Q1
river_diff = 
  group_by(housing,River)%>%summarise(avg_MedPrice=mean(MedPrice))%>% as.data.frame

river_diff



## Q2
select(housing,teacher,LSTAT)%>%plot

## cut teacher

teach_LSTAT = select(housing,teacher,LSTAT)%>%mutate(teacher_bin = ntile(teacher, 5))%>%
  select(teacher_bin,LSTAT)%>%as.data.frame
boxplot(LSTAT~teacher_bin,data = teach_LSTAT)

##Q3

library(ggplot2)
ggplot(housing, aes(factor(highwayAccess),MedPrice,color=factor(highwayAccess))) + 
  geom_boxplot(aes(fill=factor(highwayAccess)), alpha=0.3) 


