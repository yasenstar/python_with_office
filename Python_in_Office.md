 Python in Office

# Part 1 Python Basics

## Ch 1 Python Installation

### 1.1 Get to know Python

### 1.2 Install Python

### 1.3 Install Pycharm / VS Code

### 1.4 First Line of Code in Python

### 1.5 Simple Interaction

## Ch 2 Data Structure

### Six Data Type

#### 2.1 Numeric Type

##### 2.1.1 Integer
 (see:2.8.1 不可变类型 Non-Changeable Type)
##### 2.1.2 Floating
 (see:2.8.1 不可变类型 Non-Changeable Type)
##### 2.1.3 Boolean
 (see:2.8.1 不可变类型 Non-Changeable Type)
##### 2.1.4 Complex
 (see:2.8.1 不可变类型 Non-Changeable Type)
#### 2.2 String

##### 2.2.1 Characters Encode

##### 2.2.2 Strings

##### 2.2.3 转义字符

##### 2.2.4 String Index

##### 2.2.5 String Slice

##### 2.2.6 Query String Elements

##### 2.2.7 拼接字符串

##### 2.2.8 Type Converting

##### 2.2.9 Replace String

##### 2.2.10 Upper / Lower Converting

##### 2.2.11 Split String

##### 2.2.12 Formatting String

#### 2.3 List
 (see:2.8.1 可变类型 Changeable Type)
##### 2.3.1 New Create List

##### 2.3.2 Query List Elements

##### 2.3.3 Add List Elements

##### 2.3.4 Modify List Elements

##### 2.3.5 Delete List Elements

##### 2.3.6 Merge Multiple Lists

##### 2.3.7 List Element Statistics

#### 2.4 Tuple
 (see:2.8.1 不可变类型 Non-Changeable Type)
##### 2.4.1 New Create Tuple

##### 2.4.2 Access Tuple

#### 2.5 Dictionary
 (see:2.8.1 可变类型 Changeable Type)
##### 2.5.1 New Create Dictionary

##### 2.5.2 Access Dictionary Elements

###### dict_keys()

###### dict_values()

###### dict_items()

##### 2.5.3 Add Dictionary Elements

##### 2.5.4 Modify Dictionary Elements

##### 2.5.5 Delete Dictionary Elements

#### 2.6 Set
 (see:2.8.1 可变类型 Changeable Type)
##### 2.6.1 New Create Set

##### 2.6.2 交差并补
intersection(&), difference(-), union(|), complement(^)

##### 2.6.3 Add Set Elements

##### 2.6.4 Delete Set Elements

#### 2.7 None Type

### 2.8 可变类型与拷贝

#### 2.8.1 可变类型 Changeable Type

#### 2.8.1 不可变类型 Non-Changeable Type

#### 2.8.2 浅拷贝和深拷贝

##### module: copy

### 2.9 Public Methods

#### type()

#### len()

#### max(), min()

#### id()

#### ord(), chr()

#### str(), int(), float()

#### dict(), list(), tuple(), set()

#### append()

#### insert()

#### extend()

#### reverse()

#### sort()

#### count()

#### index()

#### remove()

#### get()

#### clear()

#### copy(), deepcopy()

#### pop()

#### keys(), values(), items()

#### update()

#### add()

### 2.10 运算符

#### 2.10.1 算术运算符

##### +

##### -

##### *

##### /

##### **

##### //

##### %

#### 2.10.2 比较运算符

##### >, >=

##### ==

##### <, <=

##### !=

#### 2.10.3 赋值运算符

##### =

##### +=: a=a+5 can be a += 5

##### ++: a++ can be a=a+1

#### 2.10.4 逻辑运算符

##### and

##### or

##### not

#### 2.10.5 成员运算符

##### in

##### not in

#### 2.10.6 身份运算符

##### is

##### is not

### 2.11 Traverse 遍历

### 2.12 Comprehensions 推导式

#### List Comprehensions

#### Dict Comprehensions

#### Set Comprehensions

#### Generator Comprehensions

#### Nested Comprehensions

## Ch 3 Functions

### 3.1 Basic Structure

#### 3.1.1 顺序结构

#### 3.1.2 选择结构

##### if {}
if {}

##### if {}
else {}

##### if {}
elif {}
else {}

##### if :
if not :

##### Ternary Operating 三目运算

#### 3.1.3 循环结构

##### while condition: {}

##### for i in range(): {}

### 3.2 Get to know Function

#### define function: def function_name():

### 3.3 Parameters in Function

#### 3.3.1 形参(parameter)和实参(argument)

##### A parameter is a variable in the function defintion

##### An argument is the value passed to the function when it is called

#### 3.3.2 默认参数

#### 3.3.3 不定长参数

##### *args: additional positional parameter ==> tuple

##### **kwargs: additional keyword-baesd parameter ==> dict

### 3.4 Return Value of Function

#### return

### 3.5 Pack 组包和 Unpack 解包

#### Unpacking

#### Packing

### 3.6 Variable Scope
       变量作用域

### 3.7 lambda Function 匿名函数

## Ch 4 Class and Object

### 4.1 Class and Object (Instance)

#### 4.1.1 instantiate object 实例化对象

##### Class

###### A class is a user-defined blueprint or prototype from which object are created.

###### Classes provide a means of bundling data and functionality together.

###### Creating a new class creates a new type of object, allowing new instances of that type to be made.

###### Class Definition:
class ClassName:
    # Statement

##### Object

###### An Object is an instance of a Class.
 
A class is like a blueprint while an instance is a copy of the class withActual Values.

 
An object consists ofState  (represented by the attributes of an object, also reflects the properties of an object),Behavior  (represented by the methods of an object, also reflects the response of an object to other object), andIdentity  (gives an unique name to an object and enables one object to interact with other objects)


###### Object Definition:
obj = ClassName()
print(obj.attr)

#### 4.1.2 initialization method 初始化方法:
         __init__(self [, args, ...])

#### 4.1.3 Object Property and Method 对象属性与方法

### 4.2 Private Property and Private Method
私有属性和私有方法

#### 3 types of Class resources

##### Public

###### All members in a Python class are public by default

##### Protected

###### Protected members of a class are accessible from within the class and are also available to its sub-classes

###### No other environment is permitted access to it.

###### This enables specific resources of the parent class to be inherited by the child class.

###### Python's convention to make an instance variable protected is to add a prefix _ (single underscore) to it.

##### Private

###### Private members of the class are denied access from the environment outside the class.

###### Private Property to hide Property: __(propertyName)

###### Private Method: __(methodName)

#### isinstance() built-in function

### 4.3 Magic(Dunder) Method 魔法方法

#### Dunder or Magic methods in Python are the methods having two prefixs and suffix underscores in the method name.

Dunder: means "Double Under (Underscores)"

Use "dir(int)" to list the magic functions in Python


#### General Magic Methods

Source: https://www.geeksforgeeks.org/dunder-magic-methods-python/


##### Initialization and Construction
 (see:4.3.1 Object's Lifecycle 对象的生命周期)
###### __new__()：To get called in an object's instantiation. 实例化对象时自动执行

###### __init__()：To get called by the __new__ method. 实例化对象之后自动执行

###### __del__()：It is the destructor. 对象被销毁时自动执行

##### Numeric magic methods

###### __trunc__(self): implements behavior for math.trunc()

###### __ceil__(self): implements behavior for math.ceil()

###### __floor__(self): implements behavior for math.floor()

###### __round__(self,n): implements behavior for the built-in round()

###### __invert__(self): implements behavior for inversion using the ~ operator

###### __abs__(self): implements behavior for the built-in abs()

###### __neg__(self): implements behavior for negation

###### __pos__(self): implements behavior for unary positive

##### Arithmetic operators

###### __add__(self,other): to get called on the first object when the "+" operator is used

###### __sub__(self,other): to get called when subtracting by the "-" operator

###### __mul__(self.other): to get called when multiplying by the "*" operator

###### __floordiv__(self,other): to get called when dividing by the "//" operator (whole-number division)

###### __div__(self,other): to get called when dividing by the "/" operator, it overrides the division operation for a custom object in Python 2

###### __truediv__(self,other): to get called when dividing by the "/" operator, in Python 3, it replaces __div__

###### __mod__(self,other): to get called when getting the remainder after the whole-number division by using the modulo operator "%"

###### __divmod__(self,other): return a pair (a // b, a % b) for integers.

###### __pow__(self,other,modulo): implements behavior for exponents using the ** operator

###### __lshift__(self,other): implements left bitwise shift using the << operator

###### __rshift__(self,other): implements right bitwise shift using the >> operator.

###### __and__(self,other): implements bitwise and using the & operator

###### __or__(self,other): implements bitwise or using the | operator

###### __xor__(self,other): implements bitwise xor using the ^ operator

##### String Magic Methods

###### __str__(self)：Defines behavior for when str() is called on an instance of  your class. 打印对象时自动执行

###### __repr__(self): to get called by built-in repr() method to return a machine readable representation of a type

###### __unicode__(self): this method to return an unicode string of the type.

###### __format__(self,formatstr): return a new style of string

###### __hash__(self): it has to return an integer, and its result is used for quick key comparison in dictionaries

###### __nonzero__(self): defines behavior for when bool() is called on an instance of your class

###### __dir__(self): this methods to return a list of attributes of a class

###### __sizeof__(self): it returns the size of the object

##### Comparison magic methods

###### __eq__(self,other): defines behavior for the equality operator, ==

###### __ne__(self,other): defines behavior for the inequality operator, !=

###### __lt__(self,other): defines behavior for the less-than operator, <

###### __gt__(self,other): defines behavior for the greator-than operator, >

###### __le__(self,other): defines behavior for the less-than-or-equal-to operator, <=

###### __ge__(self,other): defines behavior for the greater-than-or-equal-to operator, >=

##### Iteration magic methods

###### __iter__()：遍历对象时自动执行

###### __next__()：生成数据返回

#### 4.3.1 Object's Lifecycle 对象的生命周期

#### 4.3.2 Iterable Object 可迭代对象

##### Iterable(可迭代对象)：如果一个类实现了__iter__()的对象

##### Iterator(迭代器)：一个既实现了__iter__()又实现了__next__()的类的对象

##### Python的list、dict等容器是可迭代对象，但不是迭代器

### 4.4 Inheritance and Polymorphism
      继承和多态

#### 4.4.1 Inheritance

#### 4.4.2 Polymorphism

### 4.5 Class Method and Static Method
类方法与静态方法

#### 4.5.1 Decorators 装饰器

#### 4.5.2 Class method

#### 4.5.3 Static method

#### 4.5.4 Property decorators

## Ch 5 Other Knowledge Points

### 5.1 程序异常

### 5.2 文件读写

### 5.3 模块与包

### 5.4 常用模块

# Part 2 Use Python in Office

## Ch 6 Work with Excel

### 6.1 openpyxl

### 6.2 Open and Save

### 6.3 Work with worksheets

### 6.4 Access cell

### 6.5 Work with cell

### 6.6 Use Excel Formula

### 6.7 Configure Styles

### 6.8 Filter and Sort

### 6.9 Insert Chart / Table

### 6.10 只读只写

### 6.11 加密保护

### 6.12 xls to xlsx

## Ch 7 Work with Word

### 7.1 python-docx

### 7.2 Open and Save

### 7.3 doc to docx

### 7.4 Work with Paragraph

### 7.5 Paragraph Styles

### 7.6 Run Object

### 7.7 Unit of Length

### 7.8 Use Title

### 7.9 Work with Image

### 7.10 Work with Table

### 7.11 Page Setup

## Ch 8 Work with PPT

### 8.1 python-pptx

### 8.2 Open and Save

### 8.3 Unit of Length

### 8.4 Work with Slides

### 8,6 Use Shapes

### 8.6 使用占位符

### 8.7 Work with Text

### 8.8 Add Chart / Table

### 8.9 Work with Tables

### 8.10 Work with Images

## Ch 9 Work with PDF

### 9.1 pypdf2

### 9.2 Open and Save

### 9.3 Work with Page

### 9.4 Modify PDF

### 9.5 Extract Contents

### 9.6 Add Waterprint

### 9.7 Read/Write Meta-Data

### 9.8 Encryption / Decryption

### 9.9 PDF Converting

# Part 3 Advanced

## Ch 10 Other Processing

### 10.1 Automatic Clicking

### 10.2 Send Email

### 10.3 Web Requests

### 10.4 Scheduling Tasks

### 10.5 Graphic User Interface

### 10.6 Program Packaging
