
## 我的python学习和使用技巧
Alan Lai

* [@wp-lai](https://github.com/wp-lai)
* techwplai@gmail.com


## 文档查阅

+ 命令行：$ pydoc {what}
+ python交互环境：help({what})
+ ipython里：{what}?
+ Mac下：[Dash](https://kapeli.com/dash) + [Sublime Text](http://www.sublimetext.com) + [DashDoc](https://github.com/farcaller/DashDoc)

## 命令补齐

+ ipython
+ [Sublime Text](http://www.sublimetext.com) + [SublimeCodeIntel](https://github.com/SublimeCodeIntel/SublimeCodeIntel)


```python
adict = {'a':1,
         'b':2,
         'c':3}
```


```python
adict.keys()
```




    ['a', 'c', 'b']



## 二八模式
80%的情况下使用20%核心功能


```python
phone = "13958103975"
print "13958103975 -> #######3975"
```

    13958103975 -> #######3975


[Format string](https://docs.python.org/2/library/string.html#string-formatting)


```python
print '电话号: {}'.format(phone)
```

    电话号: 13958103975



```python
print '电话号: {:#>11}'.format(phone[-4:])
```

    电话号: #######3975


## 模式学习
归纳出不同代码想要实现的同一功能


```python
for k in adict.keys():
    print k,adict[k]
```

    a 1
    c 3
    b 2



```python
for k,v in adict.items():
    print k,v
```

    a 1
    c 3
    b 2



```python
for k in adict:
    print k,adict[k]
```

    a 1
    c 3
    b 2


## 模式学习
注意同一功能不同实现方法的细微差别


```python
alist = [1,3,2,4]
print alist.reverse()
```

    None



```python
alist = [1,3,2,4]
print reversed(alist)
```

    <listreverseiterator object at 0x1062fd150>



```python
alist = [1,3,2,4]
print alist[::-1]
```

    [4, 2, 3, 1]


## python编程技巧

+ divide and conquer
+ be explicit
