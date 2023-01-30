#!/usr/bin/env python
# coding: utf-8

# In[3]:


# program to over-ride get-item and set-item methods
class mylist:
    def __init__(self, List):
        self.List = List
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
print("the length of list is ", len(L))


# In[ ]:


return hex(self.num)
    def __oct__(self):
return oct(self.num)
    def __setitem__(self, num)n = number(-14)
print(" n is =", n.display)
print(" abs(n) is =", abs(n))
n=abs(n)
print("convertin to float", float(n))
print("converting to hexa", hex(n))
print("convrting to octa", oct(n))


# In[6]:


# to visualize iheritance flow
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(" name is", self.name)
        print(" age is", self.age)
class teacher(person):
    def __init__(self, name, age, exp, rarea):
            person.__init__(self, name, age)
            self.exp= exp
            self.rarea= rarea
    def displaydata(self):
            person.display(self)
            print("Experience is", self.exp)
            print("research area", self.rarea)
class student(person):
    def __init__(self, name, age, course, marks):
        person.__init__(self, name, age)
        self.course= course
        self.marks= marks
    def displaydata(self):
        person.display(self)
        print("Course :", self.course)
        print("Marks :", self.marks)
print("-----Teacher Class-----")
T= teacher("Mark",43, 20, "JSS")
T.displaydata()
print("-----Student Class-----")
S= student("Sucharitha Reddy",20,"CSE",75)
S.displaydata()


# In[8]:


#program to invoke __init__in multiple in heritance
class base1(object):
    def __init__(self):
        print("Base class 1")
class base2(object):
    def __init__(self):
        print("Base class 2")
class Derived(base1, base2):
    pass
D= Derived()


# In[9]:


#program to call constructor of a base class from super
class base1(object):
    def __init__(self):
        print("Base class 1")
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print("Base class 2")
class Derived(base1, base2):
    pass
D= Derived()


# In[10]:


class base1(object):
    def __init__(self):
        print("Base class 1")
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print("Base class 2")
class Derived(base1, base2):
    def __init__(self):
        super(Derived,self).__init__()
        print("Derived Class")
D= Derived()


# In[ ]:


class person:
    def name(self):
        print("Name is ....")

