dt<-read.table("~/Desktop/Rdataset/OPT.csv",sep = ";", quote=",",fileEncoding = "GB2312", header=T,fill=T)
> View(dt)
> library(ggplot2)
> ###R data type
  > ## 数字型
  > x<-1
  > x=1
  > x
  [1] 1
  > class(x)
  [1] "numeric"
  > y=1/0
  > y
  [1] Inf
  > y
  [1] Inf
  > class(y)
  [1] "numeric"
  > z="1"
  > class(z)
  [1] "character"
  > x==6
  [1] FALSE
  > #==是对x进行判断
    > x==1
  [1] TRUE
  > ## vector
    > c=("a","b","c","d")
    Error: unexpected ',' in "c=("a","
    > y=c("a","b","c","d")
    > y
    [1] "a" "b" "c" "d"
    > ##matrix
      > m=matrix(1:6,nrow=2,ncol=3,byrow=T)
    > m
    [,1] [,2] [,3]
    [1,]    1    2    3
    [2,]    4    5    6
    > m=matrix(1:6,ncol=3,nrow=2,byrow=T)
    > m
    [,1] [,2] [,3]
    [1,]    1    2    3
    [2,]    4    5    6
    > m=matrix(1:6,ncol=3,nrow=2,byrow=F)
    > m
    [,1] [,2] [,3]
    [1,]    1    3    5
    [2,]    2    4    6
    > ##只有byrow，没有bycol
      > ？matrix
    Error: unexpected input in "�"
    > ?matrix
    > help(matrix)
    > ##R语言数据读写
      > #在R中手动输入数据
      > score<-c(61,66,90,88,100)
    > points <- data.frame()
    > label=c("low","Mid","Hign")
    > Ibound=c(0,0.674,1.64,2.33)
    > Ubound=c(0.674,1.64,2.33)
    > )
Error: unexpected ')' in ")"
> points <- data.frame(
  + label=c("low","Mid","Hign")
  + Ibound=c(0,0.674,1.64,2.33)
  Error: unexpected symbol in:
    "label=c("low","Mid","Hign")
  Ibound"
  > label=c("low","Mid","High"),
  Error: unexpected ',' in "label=c("low","Mid","High"),"
  > points <- data.frame(
    + label=c("Low","Mid","Hign")
    + Ibound=c(0,0.674,1.64,2.33)
    Error: unexpected symbol in:
      "label=c("Low","Mid","Hign")
    Ibound"
    > Ibound=c(0,0.674,1.64)
    > points <- data.frame(
      + label=c("Low","Mid","Hign")
      + Ibound=c(0,0.674,1.64)
      Error: unexpected symbol in:
        "label=c("Low","Mid","Hign")
      Ibound"
      > points <- data.frame(
        + label=c("Low","Mid","Hign")
        + Ibound=c(0,0.674,1.64),
        Error: unexpected symbol in:
          "label=c("Low","Mid","Hign")
        Ibound"
        > setwd("c:")
        Error in setwd("c:") : cannot change working directory
        > install.packages("quantmod")
        Error in install.packages : Updating loaded packages
        
        Restarting R session...
        
        > install.packages("quantmod")
        trying URL 'https://mirrors.tongji.edu.cn/CRAN/src/contrib/quantmod_0.4-13.tar.gz'
        Content type 'application/octet-stream' length 142084 bytes (138 KB)
        ==================================================
          downloaded 138 KB
        
        * installing *source* package ‘quantmod’ ...
        ** package ‘quantmod’ successfully unpacked and MD5 sums checked
        ** R
        ** demo
        ** preparing package for lazy loading
        ** help
        *** installing help indices
        ** building package indices
        ** testing if installed package can be loaded
        * DONE (quantmod)
        
        The downloaded source packages are in
        ‘/private/var/folders/s8/d3b9n7yx5rg5ncc6b8l79j8h0000gn/T/Rtmp7geJ0C/downloaded_packages’
        Updating HTML index of packages in '.Library'
        Making 'packages.html' ... done
        > library(quantmod)
        Loading required package: xts
        Loading required package: zoo
        
        Attaching package: ‘zoo’
        
        The following objects are masked from ‘package:base’:
          
          as.Date, as.Date.numeric
        
        Loading required package: TTR
        Version 0.4-0 included new data defaults. See ?getSymbols.
        Learn from a quantmod author: https://www.datacamp.com/courses/importing-and-managing-financial-data-in-r
        > getSymbols("BABA")
        ‘getSymbols’ currently uses auto.assign=TRUE by default, but will
        use auto.assign=FALSE in 0.5-0. You will still be able to use
        ‘loadSymbols’ to automatically load data. getOption("getSymbols.env")
        and getOption("getSymbols.auto.assign") will still be checked for
        alternate defaults.
        
        This message is shown once per session and may be disabled by setting 
        options("getSymbols.warning4.0"=FALSE). See ?getSymbols for details.
        
        
        WARNING: There have been significant changes to Yahoo Finance data.
        Please see the Warning section of ‘?getSymbols.yahoo’ for details.
        
        This message is shown once per session and may be disabled by setting
        options("getSymbols.yahoo.warning"=FALSE).
        [1] "BABA"
        > chartSeries(BABA,subset='last 6 months')
        > addBBands()
        > library(RODBC)