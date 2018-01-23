#    第一步

###    使用解释提示符
在Python命令解释提示符输入：
            
`print("Hello World!");`

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

        print('Hello world') # print是一个函数
        
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

        age = 20
        name = 'chenpeng'
        print('{0}' was {1} years old when he wrote this book.'.format(name,age))
        print('why is {0} playing with that python?'.format(name))
        
运行结果：
![03.png](img/03.png "")








 