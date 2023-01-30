#!/usr/bin/env python
# coding: utf-8

# In[5]:


class A:
    def method_1(self):
        print("in class A")
class B:
    def method_1(self):
        print("in class B")
class Child(B,A):
    pass
ob = Child()
print(ob.method_1())


# In[11]:


n=int(input())
arr=[]
for i in range(n):
    x=input("Username:")
    y=input("Password:")
    arr.append({x:y})
print(arr)


# In[13]:


n=int(input())
arr=[]
for i in range(0,n):
    a=int(input("Username:"))
    b=int(input("password:"))
    arr.append({a:b})
print(arr)
x=input("Username:")
y=input("Password:")
f=False
for j in arr:
    try:
        b=j[x]
        f=True
        if y==b:
            print("Valid Password")
        else:
            print("Invalid Password")
    except:
        pass
if f==False:
    print("User not Found")


# In[14]:


stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)


# In[ ]:




