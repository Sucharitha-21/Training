#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def toh(n, s, d, a):
    if(n==1):
        print("source =",s," destination= ", d)
        return
    toh(n-1,s,a,d)
    print(n,s,d)
    toh(n,a,d,s)
n=4
toh(n,'A','B','C')


# In[2]:


#iteration program
def hanoi(n,A,B,C):
    if n>0:
        hanoi(n-1, A,  C, B)
        if A:
            C.append(A.pop())
        hanoi(n-1, B, A,C)
A=[1,2,3,4]
B=[]
C=[]
print(A,B,C)
hanoi(len(A),A,B,C)
print(A,B,C)


# In[1]:


# check if 2 strings mtch where 1 string  contains wildcard characters
def solve(a,b):
    n,m=len(a),len(b)
    if n==0 and m==0:
        return True
    if n>1 and a[0]=='+'and m==0:
        return False
    if(n>1 and a[0]=='?') or (n!=0 and m!=0 and a[0]== b[0]):
        return solve(a[1:],b[1:])
    if n!=0 and a[0] == '*':
        return solve(a[1:],b) or solve(a,b[1:])
    return False
x= str(input("Enter the string witth char: "))
y= str(input("Enter the string for match: "))
print("with wild characters: ", x)
print("without wild characters: ",y)
print(solve(x,y))


# In[2]:


# program to access  a class var using class obj
class abc:
    var = 22
obj = abc()
print(obj.var)


# In[3]:


# program toaccess a class member using class obj
class abc:
    var=22
    def display(self):
        print("This is class method")
obj = abc()
print(obj.var)
obj.display()


# In[12]:


# program to illustrate the constructor
#_init_()...method
class abc:
    def __init__(self,val):
        print("in class method")
        self.val=val
        print("the value is ",val)
obj=abc(10)


# In[9]:


# program to differentiate between class and obj variables
class abc():
    class_var = 0
    def __init__(self,var):
        abc.class_var +=1
        self.var=var    #obj var
        print("the obj var is: ",var)
        print("the class value of c-=var",abc.class_var)
obj1 = abc(10)
obj2 = abc(20)
obj3 = abc(30)


# In[11]:


# program illustrating a modification of numerics
class Number:
    even = 0 # default val
    def chek(self, num):
        if num%2==0:
            self.even=1
    def even_odd(self, num):
        self.check(num)
        if self.even==1:
            print('Even ',num)
        else:
            print("Odd ",num)
obj= Number()


# In[13]:


class Number:
    evens=[]
    odds=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            Number.evens.append(num)
        else:
            Number.odds.append(num)
n1 = Number(21)
n2 = Number(32)
n3 = Number(43)
n4 = Number(50)
n5 = Number(65)
print('Even numbers are ',Number.evens)
print('Odd numvers are ',Number.odds)


# In[18]:


# delete method --- c++/java analougs to destructors
# general syntax __del__
class abc():
    class_var = 0
    def __init__(self, var):
        abc.class_var+=1
        self.var = var
        print("the obj value is ", var)
        print("The class value ",abc.class_var)
    def __del__(self):
        abc.class_var-=1
        print("Object with value %d is going out of scoop",self.var)
obj1=abc(11)
obj2=abc(22)
obj3=abc(33)
del obj1
del obj2
del obj3


# In[ ]:


1 __repr__----syntax report if the objects
2 __cmp__----compares two class objects
3 __len__----len(object)
4 __call__----It acts  like  fun to call its instance
5 __it__,__le__


# In[21]:


# program to to dempnstrate get and set items in a list 
class numbers:
    def __init__(self,mylist):
        self.mylist= mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index] = val
numlist = numbers([1,2,3,4,5,6,7,8,9])
print(numlist[3])
print(numlist.mylist)
numlist[3] = 10
print(numlist.mylist)
print(numlist[3])


# In[25]:


class ABC():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var - obj.var
obj = ABC("abbcdef",10)
print("The value stored in obj is: ",repr(obj))
print("The length of the name stored in obj: ",len(obj))
obj1 = ABC("ghijkl",1)
val = obj.__cmp__(obj1)
if val==0:
    print("Both values are equal")
elif val==-1:
    print("1st value is less than 2nd")
else:
    print("2nd value is less than 1st ")


# In[34]:


#is for illustrating use of a private method
class abc:
    def __init__(self,var):
        self._var=var
    def __display(self):
        print("This from class method ,var=" ,self._var)
obj=abc(10)
obj._abc__display()


# In[33]:


class abc():
    def __init__(self, var):
        self.var=var
    def display(self):
        print("var is =",self.var)
    def add_2(self):
        self.var +=2
        self.display()
obj = abc(10)
obj.add_2()


# In[35]:


#programto show how a class method calls a function which defined in the global name space
def scale_10(x):
    return x*10
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is =", self.var)
    def modify(self):
        self.var = scale_10(self.var)
obj = abc(10)
obj.display()
obj.modify()
obj.display()


# In[ ]:


# built-in attributes
# forget set and del
1. hasattr(obj, name) - checks obj possesses the attributes values or not
1. getattr(obj, name[,default])
3. setattr(obj, name, value)-- which is used to set an attribute of the obj
4. delattr(obj, name)


# In[ ]:


built-in class attributes
1. .__dict__
2. .__doc__
3. .__name__
4. .__bases__


# In[40]:


def fib(n):
    if n<2:
        return 1
    return(fib(n-1)+fib(n-2))
n = int(input())
for i in range(n):
    print(fib(i))


# In[42]:


a=[]
for i in range(1500,2700):
    if i%7==0 and i%5==0:
        a.append(i)
print(a)


# In[3]:


#Abstract class
#it the process of handling the information by hiding
#informal or unnecesary for the user
class fruit:
    def taste(self):
        raise NotImplementedError()
    def rich(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()
class mango(fruit):
    def taste(self):
        return "sweet"
    def rich(self):
        return "Vitamin A"
    def color(self):
        return "Golden yellow color"
class orange(fruit):
    def taste(self):
        return "sour"
    def rich(self):
        return "Vitamin C"
    def color(self):
        return "Orange"
Alphanso=mango()
print(Alphanso.taste(),Alphanso.rich(),Alphanso.color())
Orange=orange()
print(Orange.taste(),Orange.rich(),Orange.color())


# In[10]:


#program to interviene polymorphysim on a complex number
class Complex():
    def __init__(self):
        self.real = 0
        self.img = 0
    def setValue(self, real, img):
        self.real = real
        self.img = img
    def ___add__(self,c):
        temp = Complex()
        temp.real = self.real+c.real
        temp.img = self.img+c.img
        return temp
    def display(self):
        print("(", self.real, "+", self.img, ")")
c1= Complex()
c1.setValue(1,2)
c2= Complex()
c2.setValue(3,4)
c3=c1+c2
print("result is...")
c3.display()


# In[11]:


'''
+      __add__
+=     __iadd__
-      __sub__
-=     __isub__
*      __mul__
*=     __imul__
/      __truediv__
/=     __idiv__
**     __pow__
**=    __ipow__
%      __mod__
%=     __imod__
>>     __rshift__
>>=    __irshift__
&      __and__
&=     __iand__
|      __or__
|=     __ior__
^      __xor__
^=     __ixor__
~      __invert__
~=     __iinvert__
>      __gt__
<      __lt__
>=     __ge__
<=     __le__

'''


# In[12]:


#program that has abstract class to derive 2 classes
   #rectangle and triangle from polyon class
   #write the methods to get their details and dimensions
   # and hence calcualte the area respectively
class polygon():
   def get_data(self):
       raise notImplementedError()
   def area(self):
       raise notImplementedError()
class rectangle(polygon):
   def get_data(self):
       self.length= float(input("Enter rectangle length"))
       self.breadth= float(input("Enter rectangle breadth"))
   def area(self):
       return self.length * self.breadth
class triangle(polygon):
   def get_data(self):
       self.base= float(input("Enter triangle base"))
       self.height= float(input("Enter triangle height"))
   def area(self):
       return 0.5*self.base * self.height
R = rectangle()
R.get_data()
print("Area of a rectangle ", R.area())
T = triangle()
T.get_data()
print("Area of a triangle ", T.area())


# In[13]:


# encapsuling public members
class pub:
    def __init__(self, name, num):
        self.num = name
        self.num = num
    def Num(self):
        print("Roll num is ", self.num)
obj = pub("Harry", 229)
obj.Num()


# In[15]:


#program to overload the __call__method
class multi:
    def __init__(self , num):
        self.num = num
    def __call__(self, O):
        return self.num * O
x= multi(10)
print(x(5))


# In[ ]:


# program to over-ride get-item and set-item methods
class mylist:
    def __init__(self, List):
        self.List = list
    def __getitem__(self, index):
        return self.List[index]
    def __setitem__(self,index,num):
        self.List[index]=num
    def __len__(self):
        return len(self.List)
    def display(self):
        print(self.List)
L = mylist([1,2,3,4,5,6,7,8,9])
print("List is.........")
L.display()
index = int(input("Enter the index of the list"))
print(L[index])
index = int(input("Enter the index of the list"))
num = int(input("Enter the position u want to modify"))
L[index] = num
L.display()
print("the length of list is ", len())


# In[ ]:




