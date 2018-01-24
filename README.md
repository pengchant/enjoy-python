***文本为《python简易教程》的自学笔记***

#    第一步

###    使用解释提示符
在Python命令解释提示符输入：
            
```python
print("Hello World!");
```

结果

![01.png](img/01.png "")

### 如何退出解释器提示符
>    GNU/LINUX 或者 OS X上的shell程序，`ctrl+d' 或者输入 `exit()`

>    WINDOWS: `ctrl+z [enter]` 退出

### 使用编辑器

这里使用了pycharm

![02.png](img/02.png "")


#    基础

### 注释
例子：

        
```python
print('Hello world') # print is a function
```
        
### 字面常量

>    字面常量的例子是诸如23 4 这样的数字或者`这是一个文本` 这样的文本

### 数字

>    数字主要分两种
>    *    整数(Integers)
>    *    浮点数(Floats)

### 字符串

>字符串(string) 是字符(characters)的序列(sequence)
>    *    单引号,可以使用单引号来指定字符串,比如说`'天行所向利剑凌空'`
>    *    双引号,被双引号和单引号括起来的字符串其工作机制是一样的,比如说`"what's your name?`
>    *    三引号,在三引号之间的实际上是多行字符串，另外可以再三引号之间自由地使用单引号和双引号        

### 字符串是不可变的

这意味着一旦你创建了一串字符串，你就不能改变他

### 格式化方法 

有时候，我们想从其他信息中构建字符串。利用formate函数

```python
age = 20
name = 'chenpeng'
print('{0}' was {1} years old when he wrote this book.'.format(name,age))
print('why is {0} playing with that python?'.format(name))
```

运行结果：

![03.png](img/03.png "")

但是，数字是可选的，同样的也可以写成

```python
print('{} was {} years old when he wrote this book'.format(name,age))
print('why is {} playing that with python?'.format(name))
```

formate 还有更详细的用法：

```python
        # 对于浮点数，'0.333' 保留小数点(.)后三位
        print('{0:.3f}'.format(1.0/3));
        # 使用下划线填充文本，并保持文字处于中间位置
        # 使用(^)定义'___hello___'字符串长度为11
        print('{0:_^11}'.format('hello'))
        #基于关键词输出'Swaroop wrote A Byte of Python
        print('{name} wrote {book}'.format(name="xiaopeng",book="enjoy-python"))
```
        
注意print()函数，最后会以一个不可见的"新一行"字符(\n)结尾,为了防止打印过程中出现
换行,可以通过`end`指定空白结尾:

```python
        print('a',end='')
        print('b',end='')
```
        
输出结果:

        ab
        
或者你可以通过end指定空格结尾:

```python
        print('a',end=' ')
        print('b',end=' ')
        print('c')
```
        
输出结果:

        a b c

###    转义序列(Escape Sequence)

如果希望生成的字符串中包含(')、(\)以及其他诸如控制字符串格式的(\n)、(\t)等需要用到转义序列

比如要输出`what's your name` 

应该这样写 `'what\'s your name'`

利用`\n`换行,`This is the first line \n This is the second line'`

***\***还有一个特殊的用法，用在末尾表示字符串在下一行继续:

```python
        "This is the first sentence.\
        This is the second sentence."
```

相当于:

```python
        "This is the first sentence.This is the second sentence."
```
     
###    原始字符串

如果你需要指定一些未经处理的字符串,比如转义序列,可以在字符串前加上`r`或者`R`

```python
        r"Newlines are indicated by \n"
```
        
###    变量

使用字面量无法满足我们开发的需求， 这时候就需要使用变量(veriables).

###    标识符命名

*    第一个字符必须是字母表中的字母(大小写ASCII或者Unicode或者_)
*    标识符的其他部分可由字符、下划线、数字组成
*    标识符区分大小写

###    数据类型

变量可以将各种形式的值保存为不同的数据类型,基本的数据类型包括数字和字符串，在后面我们将会讨论通过类(Classes)来创建我们自己的数据类型.

###    对象


需要记住python将程序中任何内容统称为对象(Object).这是一般意义的叫法。我们通常以某对象(object)相称，而非某东西(something)
 
###     如何编写python程序

案例：使用变量和字面变量
 
```python
# 文件名:var.py

i = 5
print(i)
i = i+1
print(i)

s = '''This is muti-line string.
This is the second line.'''
print(s)
```

输出：

        5
        6
        This is muti-line string.
        This is the second line.
        
>    变量秩序被赋值某一个值，不需要声明或定义数据类型

###    物理行与逻辑行

物理行(Physical Line)是指在编写程序时你所看到的内容。
逻辑行(Logical Line)是指Python所识别的单个语句。
实际上，python暗含这样一个期望鼓励每一行使用一句独立的语句从而使得代码更加可读
如果你希望在一行物理行中指定多行逻辑行，那么你必须使用`;`来表示该行或者语句的结束.

```python
i = 5
print(i)
```
实际上等价于
```python
i = 5;
print(i);
```
同样可以看作
```python
i = 5;print(i);
```
也与这一写法相同
```python
i = 5;print(i)
```
> 实际上不应该使用分号，在python程序中大多不存在`;`的使用，如果你有一行非常长的代码，你可以通过反斜杠`\`来将其拆分成多个物理行.这被称之为**显式连接**(Explicit Line Joining):

```python
s = 'This is a string.\
This continues the string.'
print(s)
```
结果输出：
        This is a stirng.This continues the string.
        






 