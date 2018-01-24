***文本为《python简易教程》的自学笔记***


#   **第一步**

###    **使用解释提示符**
在Python命令解释提示符输入：
            
```python
print("Hello World!");
```

结果

![01.png](img/01.png "")



### **如何退出解释器提示符**
>    GNU/LINUX 或者 OS X上的shell程序，`ctrl+d' 或者输入 `exit()`

>    WINDOWS: `ctrl+z [enter]` 退出


### **使用编辑器**

这里使用了pycharm

![02.png](img/02.png "")


---
#    **基础**


### **注释**
例子：

        
```python
print('Hello world') # print is a function
```
   
   
### **字面常量**

>    字面常量的例子是诸如23 4 这样的数字或者`这是一个文本` 这样的文本


### **数字**

>    数字主要分两种
>    *    整数(Integers)
>    *    浮点数(Floats)


### **字符串**

>字符串(string) 是字符(characters)的序列(sequence)
>    *    单引号,可以使用单引号来指定字符串,比如说`'天行所向利剑凌空'`
>    *    双引号,被双引号和单引号括起来的字符串其工作机制是一样的,比如说`"what's your name?`
>    *    三引号,在三引号之间的实际上是多行字符串，另外可以再三引号之间自由地使用单引号和双引号        


### **字符串是不可变的**

这意味着一旦你创建了一串字符串，你就不能改变他


###  **格式化方法**

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


###    **转义序列(Escape Sequence)**

如果希望生成的字符串中包含(')、(\)以及其他诸如控制字符串格式的(\n)、(\t)等需要用到转义序列

比如要输出`what's your name` 

应该这样写 `'what\'s your name'`

利用`\n`换行,`This is the first line \n This is the second line'`

还有一个特殊的用法，用在末尾表示字符串在下一行继续:

```python
        "This is the first sentence.\
        This is the second sentence."
```

相当于:

```python
        "This is the first sentence.This is the second sentence."
```
     

###    **原始字符串**

如果你需要指定一些未经处理的字符串,比如转义序列,可以在字符串前加上`r`或者`R`

```python
        r"Newlines are indicated by \n"
```

    
###    **变量**

使用字面量无法满足我们开发的需求， 这时候就需要使用变量(veriables).


###    **标识符命名**

*    第一个字符必须是字母表中的字母(大小写ASCII或者Unicode或者_)
*    标识符的其他部分可由字符、下划线、数字组成
*    标识符区分大小写


###    **数据类型**

变量可以将各种形式的值保存为不同的数据类型,基本的数据类型包括数字和字符串，在后面我们将会讨论通过类(Classes)来创建我们自己的数据类型.


###    **对象**

需要记住python将程序中任何内容统称为对象(Object).这是一般意义的叫法。我们通常以某对象(object)相称，而非某东西(something)


###     **如何编写python程序**

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


###    **物理行与逻辑行**

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
        
类似地，

```python
i = \
5
```
等价于
```python
i = 5
```

>    在某些情况下，会存在一个隐含的交涉，允许你不用反斜杠这一情况即以括号开始，它可以是方括号或者花括号，但不能是结束括号，这称为**隐式连接**(Implicit Line Joining)


### **缩进**

空白区在python中是非常重要的。空白区在各行的靠头非常重要被称为(Indentation).在逻辑行的开头留下空白区(使用空格或者制表符)用以确定各逻辑行的缩进级别，后者可以确定语句的分组。这表示放置在一起的语句必须要有相同的缩进，我们把每一组这样的语句称为**块**(block)

错误的缩进会导致错误

```python
i = 5
 print('Value is',i)
print('I repeat,the value is',i)
```
![04.png](img/04.png "")


>如何缩进?

>使用四个空格来缩进，这是python官方的建议


---
#    **运算符与表达式**



我们所编写的大多数语句(逻辑行)都包含了表达式(Expressions).
一个表达式的简单的例子就是`2+3`.表达式，可以拆分为
*    运算符(Operators)
*    操作数(Operands)

在`2+3`这样的表达式里，`+`就是运算符，`2`和`3`就是操作数


###    **运算符**

下面来简要的了解各类运算符以及他们的用法

![05.png](img/05.png "")

下面是运算符的速览

*    `+` （加）
        *    两个对象相加
        *    `3+5`则输出`8`，`'a'+'b'` 输出 `'ab'` 

        
*    `-` （减）
        *    从一个数中减去另一个数,如果第一个操作数不存在，假定为0
        *    `-5.2` 将输出一个负数
 
       
*    `*` （乘）
        *    给出两个数的乘积，或者返回字符串重复指定次数后的结果
        *    `2*3` 输出 `6` . `'la'*3` 输出 `'lalala'`.
    
    
*    `**`（乘方）
        *    返回x的y次方
        *    `3**4` 输出 `81` （即`3*3*3*3`）
     
   
*    `/` （除）
        *    x除以y
        *    `13/3` 输出 `4.333333333333`


*    `//` （整除）
        *    x除以y并对结果向下取整至最接近的整数
        *    `13//4` 输出 `4`.
        *    `-13//4` 输出 `-5`
       

*    `%` （取模）
        *    返回除法之后的余数
        *    `13%5` 输出 `1` 


*    `<<` （左移）
        *    将数字的位想左移动指定的位数
        *    `2<<2` 输出 `8` 


*    `>>` （右移）
        *    将数字的位向右移动指定的位数
        *    `11>>1` 输出 `5`


*    `&` （按位与）
        *    对数字进行按位与操作
        *    `5&3` 输出 `1`


*    `|` （按位或）
        *    对数字进行按位或操作
        *    `5|3` 输出 7


*    `~` （按位取反）
        *    `~5` 输出 -6 
        *    x的取反的结果为 `-(x+1)`


*    `<` （小于）
        *    返回x是否小于y，所有比较的结果返回`True`或者`False`，注意首字母为大写
        *  `5<3` 输出 `False`
        *  比较可以任意组成链接:`3<5<7` 返回 `True`


*    `<=` （小于等于）
        *    返回x是否小于或等于y
        *    `x = 3;y = 6;x<=y` 返回 `True`


*    `>=` （大于等于）
        *    返回x是否大于或者等于y
        *    `x = 4;y = 3;x>=3` 返回 `True`


*    `==` （等于）
        *    比较两个对象是否相等
        *    `x = 2;y = 2;x == y` 返回 `True`
        *    `x = 'str';y = 'stR';x == y` 返回 `False`
        *    `x = 'str';y = 'str';x == y` 返回 `True`


*    `!=` （不等于）
        *    比较两个对象是否不相等
        *    `x = 2;y = 3;x!=y` 返回 `True`


*    `not` （布尔"非"）
        *    如果x是`True`,返回 `False`，同理反之亦如是
        *    `x = True;not x` 返回 `False`


*    `and` （布尔"与"）
        *    若x为`False`,则` x and y `返回 `False`,否则返回`y`的计算值
        *    若x为`False`,` x = False;y = True; x and y `此时python将不会计算y因为它已经了解and表达式的左侧为`False`，意味着整个表达式都是`False`,这种情况为**短路运算**(Short-circuit Evaluation)


*    `or` （布尔"或"）
        *    如果x为` True `,返回 ` True `，否则返回y的计算值
        *    ` x = True;y = False; x or y ` 返回` True `,在这里短路运算同样适用.
   

### **数值运算与赋值的快捷方式**

> 变量 = 变量 运算 表达式 

``` python
a = 2
a = a*3
```

> 变量 运算 = 表达式 

```python
a = 2
a *= 3
```

### **求值顺序**

下表罗列了python的运算的优先级

![yunsuan01.png](img/yunsuan01.png "")
![yunsuan02.png](img/yunsuan02.png "")

  
### **改变运算顺序**

可以使用括号来使得表达式更加易读


### **结合性**

运算符通常由左至右结合


### **表达式**

例子

```python
length = 5
breadth = 2

area = length*breadth
print('Area is ',area)
print('Perimeter is ',2*(length+breadth))
```

输出

  ![ex.png](img/ex.png "")
  


---
#    **控制流**

python中有三种控制流语句
*    if
*    for
*    while


### **if语句**

案例，其中else从句是可选的

```python
number = 23
guess = int(input('Enter an integer:'))

if guess == number:
    print('Congratulations,gu guessed it.')
    print('(but you do not win any prizes!)')
elif guess<number:
    print("No,it is a litter higher than that")
else:
    print('No,it is a little lower than that!')

print('Done')
```

输出

![cg.png](img/cg.png "")
![lr.png](img/lr.png "")


> python 中不存在switch语句


### **while 语句**

案例：

```python
number = 23
running = True

while running:
    guess = int(input('enter an integer :'))

    if guess == number:
        print('success!,you guessed it.')
        running = False
    elif guess<number:
        print('No,it is little higher!')
    else:
        print('No,it is little lower!')
else:
    print('The while loop is over.')

print('done')
```

结果：

![while-01.png](img/while-01.png "")

> 可以在while循环中使用else语句


### **for 循环**

```python
for i in range(1,5):
    print(i)
else:
    print('The for loop is over')

```
输出的结果为

![for.png](img/for.png "")

>在这个例子中我们使用了内置的`range`函数生成这一数字序列。range(1,5)将会产生[1,2,3,4]。如果我们向range提供第三个参数，这个数字将成为步长，比如range(1,5,2),将会产生[1,3],特别注意不包括第二个数字在内，换做数学语言来讲是左边开区间，右边闭区间，第三个数为步长。



### **break 语句**


`break`语句用以中断循环语句，也就是终止循环的语句。

> 有一点需要注意的是，如果你中断了比如for和while循环，那么，任何相应循环中的else块都将不会执行

案例：

```python
while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    print('Length of the string is ',len(s))
print('Done')
```
运行结果：

![break.png](img/break.png "")


###  **continue 语句**

所谓continue就是告诉python跳过当前循环中的剩余的语句继续下一个循环。

案例：

```python
while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    if len(s)<3:
        print('Too small')
        continue
    print('Input is out of sufficient length')
```

运行结果：

![continue.png](img/continue.png "")

> 注意 continue 同样能够适用于for循环



#    **函数**

所谓函数(Functions)就是可重复使用的程序片段。
通过函数名在程序的任何地方来运行代码块，并且可以执行任意次数，这就是所谓的调用(Calling)函数

函数可以通过`def` 来定义
> 函数定义形式:

        def say_hello():
            # do something...
        # end function
>函数的调用:  

        say_hello() 
        


### **函数参数**

函数中的参数通过防止在用以定义函数的一对括号中指定。

特别地：

**在定义函数时候给的名称叫做"形参"(Parameters)**

**在调用函数时所提供给函数的值称为"实参"(Arguments)**

案例：

```python
def print_max(a,b):
    if a>b:
        print(a,'is maximum')
    elif a == b:
        print(a,'is equal to',b)
    else:
        print(b,'is maximum')


print_max(3,4)

x = 5
y = 7

print_max(x,y)
```

运行结果：

![function.png](img/function.png "")

> 第一次调用我们以实参的形式直接向函数提供这一数字，第二次调用时候，我们使用变量来作为实参调用函数，是的将实参x赋值给形参a，两次print_max都以相同的方式工作


### **局部变量**

> 当你在一个函数的定义中声明变量，他们不会以任何方式与身处函数之外具有相同名称的变量产生任何的关系，也就是说，这些变量名，**只存在函数这一局部(local)**.这被称之为**作用域(Scope)**.

案例:

```python
x = 50

def func(x):
    print('x is ',x)
    x = 2
    print('Changed local x to ',x)

func(x)
print('x is still ',x)
```

结果：

![function_local.png](img/function_local.png "")

> 实际上x的值并不会收到调用的函数中的局部变量的影响.


### **`global` 语句**


如果你想给一个在程序顶层的变量赋值，你必须告诉python这是一个全局(Global)的变量不是局部变量,我们通常需要通过global语句来完成这件事情.因为，你不看为一个定义于函数之外的变量赋值.

案例：

```python
x = 50

def func():
    global x

    print('x is ',x)
    x = 2
    print('changed global x to ',x)

func()
print('value of x is ',x)
```

运行结果：

![function_global.png](img/function_global.png "")

> 不难看出和上一个例子不同这里的x已经改变了,如果语句中不知一个全局变量，你可以这样写 `global x,y,z`



###   **默认参数值**

对于有些函数你可能希望是一些参数可选并使用默认值，你可以在函数定义时候，附加一个赋值运算符(`=`)来为参数制定默认的参数值.

案例:

```python
def say(message,times=1):
    print(message*times)

say('Hello')
say('World',5)
```

运行结果：

![function_default.png](img/function_default.png "")

> 注意！
> 在函数列表中，拥有默认参数值参数不能位于没有默认参数值的参数之前.
> 举例来说,def func(a,b = 5)是合法的，但def func(a = 5,b)是无效的


### **关键字参数**

假设你有一些许多参数的函数，但是，你不可能为每一个参数都赋值，这样看起来很傻，我们只希望对其中某些关键的参数来给这些参数赋值，这就是**关键字参数(*Keywrod Arguments*)**

案例：

```python
def func(a,b = 5,c =10):
    print('a is ',a,' and b is ',b,'and c is ',c)

func(3,7)
func(25,c = 24)
func(c = 50,a = 100)
```

运行结果：

![function_keyword.png](img/function_keyword.png "")

> 实际上可以看到func(3,7),参数a获得了3，参数b获得7，而c获得了函数定义时候的默认值
>第二次调用，参数a获得25，但是这时候我们不想给b赋值，我们通过关键字参数来直接给c赋值，从而打破了函数调用时参数顺序的限定
>同理第三次调用，我们直接将c先赋值，再对a赋值，这也是允许的，所以python的语法还是很灵活的!记住这是**关键字参数**带给我们的便利


### **可变参数**

有时你可能想定义的函数里面能够有任意数量的变量，也就是参数数量是可变的，这可以通过使用型号来实现

案例：

```python
def total(a = 5,*numbers,**phonebook):
    print('a',a)

    for single_item in numbers:
        print('single_item',single_item)

    for first_part,second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack = 1123,John = 2231,Inge=1560))
```

结果：

![function_varargs.png](img/function_varargs.png "")

> 当我们声明\*param的星号参数时，从此处开始知道结束的所有位置参数(*Positional Arguments*)都将被收集并汇集成一个称为"param"的**元组(*Tuple*)**

> 当我们声明\*\*param的双星号参数时,从此处来时直至结束的所有的关键字参数都将被收集并汇集成一个名为Param的**字典(*Dictionary*)**


###     **`return` 语句**

`return` 语句用于从函数中返回，也就是中断函数.

案例：

```python
def maximum(x,y):
    if x>y:
        return x
    elif x == y:
        return "The numbers are equal "
    else:
        return y

print(maximum(2,3))
```

运行结果：

![function_return.png](img/function_return.png "")

> 要注意如果return 没有搭配任何一个值则代表着 None.
None 在Pyton中是一个特殊的类型，代表着虚无。
每一个函数都在其末尾隐含了一句`return None`,除非你写了你自己的`return` 语句.

> 另外有一个名为max内置函数已经实现了找最大值的功能，尽可能使用这一内置函数



###    **DocStrings**

**DocStrings**是一款甚是优美的功能，能够帮助你更好地记录程序并让其更加易于理解。

案例：

```python
def print_max(x,y):
    '''prints the maximum of tow mumbers.
    The tow values must be integers.'''

    x = int(x)
    y = int(y)

    if x>y:
        print(x,' is maximum')
    else:
        print(y,' is maximum')

print_max(3,5)
print(print_max.__doc__)
```

结果：

![function_docstring.png](img/function_docstring.png "")

>我们可以通过函数的 `__doc__` 的属性来获取函数print_max文档的字符串属性，自动化工具可以用这种方式来检索你程序中的文档，所以墙裂建议编写的所有重要的函数配以文档字符串。python发型版本中附带的pydoc命令和help()使用文旦字符串的方式类似

---

#    **模块**

如果你想在你所编写的程序中重用一些函数的话，应该怎么办？答案是模块(Modules).

首先我们来了解如何使用标准款模块

```python
import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is ',sys.path,'\n')
```

输出：

![module_using_sys.png](img/module_using_sys.png "")



### **按字节编码的.pyc文件**

导入一个模块是一件代价高昂的事情，因此python引入了一些技巧来使其能够更加快速的完成。其中一种方式就是创建按字节码编译的***(byte-compiled)***文件，这些.pyc文件是独立于运行平台的

> 这些.pyc文件通常会创建在对应的.py文件所处的目录中，如果python没有相应的权限对这一目录进行写入文件的操作，那么.pyc文件将不会被创建.



### **from..import 语句**

如果希望直接将argv的变量导入自己的程序，可以使用`from sys import argv`这一语句来完成.

> 警告：一般来说，应该尽量避免使用from...import 语句，而去使用import语句,这是为了避免在自己的程序中出现名称冲突，也为了使程序更加的可读

案例

```python
from math import sqrt
print('square root of 16 is ',sqrt(16))
```



### **模块的 __name__语句**

每一个模块都有一个名称，而模块中的语句可以找到它们所处的模块的名称，这对于确定模块是独立运行的还是被导入进来的运行的这一特定目的来说大为有用.

案例：

```python
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('Iam being imported from another module')

```

结果

![module_using_name.png](img/module_using_name.png "")


###    **编写你自己的模块**

在Python中每一个python程序同时也是一个模块。只需要保证它以.py为拓展名即可

案例(保存为 mymodule.py)

```python
def say_hi():
    print('Hi,this is mymodule speaking.')

__version__ = '0.1'
```

另一个模块(保存为 mymodule_demo.py)

```python
import  mymodule

mymodule.say_hi()
print('Version',mymodule.__version__)

```

输出：

        Hi,this is mymodule speaking.
        Version 0.1

下面是` from...import` 语法的版本(保存为 `mymodule_demo2.py`)

```python
from mymodule import say_hi,__version__

say_hi()
print('Version',__version__)

```

> 这里需要注意的是，如果导入到mymodule中已经存在了\_\_version\_\_这一名称，那将会产生冲突。所以我们大都推荐最好去使用import 语句，尽管看起来代码稍微长一些。

你还可以使用：

```python
from mymodule import *
```
这将导入诸如 `say_hi` 等所有公共名称，但不会导入\_\_version\_\_名称,因为后者以双下划线开头.

> 警告：应该避免使用import-star 这种形式



###    **dir 函数**

内置的 `dir()` 函数能够返回由对象所定义的名称列表.
如果该对象是一个模块,则该列表会包括函数内所定义的函数、类与变量

另外，该函数还接受参数。如果参数时模块名称，函数将返回这一指定模块的名称列表。如果没有提供参数，函数将返回当前模块的名称列表。

案例：

```python
import sys
dir(sys)
```

返回的结果：

![dir.png](img/dir.png "")

下面给出当前模块的属性名称
```python
dir()
```

返回的结果

![dir02.png](img/dir02.png "")

接着创建一个新的变量

```python
a = 5
```

返回的结果：

![dir03.png](img/dir03.png "")

删除或者移除一个名称

```python
del a
```

返回的结果：

![dir04.png](img/dir04.png "")

> 同时还有一个` vars() `函数也可以返回给你这些值的属性，但只是可能，并不对所有的类都能正常工作

###    **包**

代码必须加以有效的管理，学过java、c++的同志们应该知道代码必须有章法，否则就是一盘散沙不能够真正凝聚力量来解决大规模的问题。python中，变量通常位于函数的内部，函数和全局变量通常位于模块内部。如果你希望组织起来，这就是**包(Package)**登场的时刻.

包是指一个包含模块与一个特出的\_\_init\_\_.py文件的文件夹，后者想Python表面这一文件夹是特别的，因为其包含了python模块.

假设你想创建一个"world"的包，其中还包含着"asia"、"afica"等包，并且这些子包都包含了诸如"india"、"madagascar"等模块.

        - <some floder present in the sys.path>/
            - world/
                - __init__.py
                - asia/
                    - __init_.py
                    - india/
                        - __init_.py
                        - foo.py
                - africa/
                    - __init__.py
                    - madagascar/
                        - __init__.py
                        - bar.py

> 包是一种能够方便地分层组织模块的方式，你将在标准库中看到许多诸如此类的实例


---

#    **数据结构**

数据结构(Data Structures)是用来存储一些相关数据的集合。

在python中有四种内置的数据结构
*    列表(List)
*    元祖(Tuple)
*    字典(Dictionary)
*    集合(Set)

###    **列表(List)**

列表是一种用于保存一些**有序**项目的集合.python中需要你在它们之间多加上一个逗号，项目的列表应该用方括号括起来，这样python才能理解你正在指定一张列表.一旦你创建了一张列表你可以添加、删除、搜索列表中的项目.我们说列表是一种可变(Mutable)的数据类型，这种数据类型是可以被改变的.

###    **有关对象和类的快速介绍**

列表是使用对象与类的实例。当我们启用一个变量i并将整数5赋值给它时，你可以认为这是在创建一个int类之下的对象i.

一个类也可以带有方法(Method),也就是说对这个类定义仅对于它启用某个函数.例如python 为 list 类提供了一种 append 方法,它能够允许你向列表末尾添加一个项目.例如` mylist.append('an item') `将会向mylist添加一串字符串.

一个类同样也可以具有字段(Field),它是只为该类定义且为该类所用的变量.字段同样可以通过.来访问，比如` mylist.field `.

案例(保存为 ` ds_using_list.py `)

```python
shoplist = ['apple','mango','carrot','banana']

print('I have',len(shoplist),' items to purchase')

print('These items are:',end=' ')
for item in shoplist:
    print(item,end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now ',shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is ',shoplist)

print('The first item I will buy is ',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the',olditem)
print('My shopping list is now',shoplist)

```

输出结果：

![ds_using_list.png](img/ds_using_list.png "")

你可以想列表中添加任何类型的对象，包括数字，甚至是其他列表
我们还使用 for...in 循环来便利列表中的每一个项目
这里注意在调用print函数时我们使用end参数，这样就能够通过一个空格来完成输出工作而不是通常的换行.
接下来，如我们讨论的那段，我们通过列表对象中的append方法向列表中添加一个对象.
>列表是可变的，而字符串是不可变的
当我们需要删除列表中的元素时，我们使用`del`语句来实现这一需求.

###    **元组**

元素(Tuple)用于将多个对象保存在一起。类似于列表但是不能提供列表类能够提供给你的广泛的功能。元素的一大特征类似于字符串，他们不可变.你不能编辑或者更改元组.

案例(ds_using_tuple.py):

```python
zoo = ('python','elephant','penguin')
print('Number of animals in the zoo is ',len(zoo))

new_zoo = 'monkey','camel',zoo
print('Number of cages in the new zoo is ',len(new_zoo))
print('All animals in new zoo are ',new_zoo)
print('Animals brought from old zoo is ',new_zoo[2])
print('Last animal brought from old zoo is ',new_zoo[2][2])
print('Number of animals in the new zoo is ',len(new_zoo)-1+len(new_zoo[2]))
```

输出结果：

![tuples.png](img/tuples.png "")

> 如同我们在列表里所做的那般，我们可以通过在方括号中指定项目所处的位置来访问元祖中的各个项目。这种使用方括号的形式被称为**索引(Indexing)**运算符.
>
> 一个空的元素由一对圆括号组成，就像 `myempty=()` 这样.然而，一个只拥有一个项目的元祖并不像这样简单.你必须在第一个项目的后边加上一个逗号来指定它，如此一来python才可以识别出在这个表达式想表达的是一个元组还是一个对象.如果你想指定一个包含项目2的元组你必须指定`singleton=(2,)`






























 