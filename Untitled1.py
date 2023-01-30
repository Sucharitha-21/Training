#!/usr/bin/env python
# coding: utf-8

# In[4]:


rows = int(input("Enter the no of rows:"))
i=1
while i<rows:
    j=rows
    while j>i:
        print(' ', end=' ')
        j-=1
    print('*', end=' ')
    k=1
    while k<2 *(i-1):
        print(' ', end=' ')
        k+=1
    if i==1:
        print()
    else:
        print('*')
    i+=1
i= rows -1
while i>=1:
    j=rows
    while j>i:
        print(' ', end=' ')
        j-=1
    print('*' ,end=' ')
    k=1
    while k<2 *(i-1):
        print(' ',end=' ')
        k+=1
    if i==1:
        print()
    else:
        print('*')
    i-=1


# In[6]:


rows = 5
k = 2 * rows-2
for i in range(0,rows):
    for j in range(0,k):
        print(end=' ')
    k=k-1
    for j in range(0, i+1):
        print('*',end=' ')
    print(" ") 
k = rows-2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=' ')
    k=k+1
    for j in range(0,i+1):
        print('*',end=' ')
    print(' ')
        


# 

# In[5]:


word = "Canada"
x=" "
for i in word:
    x+=i
    print(x)


# In[9]:


a = 65
r = 7
for i in range(0,r):
    for j in range(0,i+1):
        ch = chr(a)
        print(ch, end=' ')
        a+=1
    print(" ")


# In[13]:


a = 65
r = 5
m = (2*a) -2
for i in range(0, r):
    for j in range(0, m):
        print(end=" ")
    m=m-1
    for j in range(0, i+1):
        ch = chr(a)
        print(ch, end=' ')
        a+=1
    print(" ")


# In[14]:


rows = 10
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(i*j, end=" ")
    print()


# In[15]:


#function
'''
def username(arg1, arg2, ...):
------
------
return 
'''
def diff(a,b):
    return a-b
x= 20
y= 10
operation = diff
print(operation(x,y))


# In[16]:


#display str in n no of lines
def fun():
    for i in range(5):
        print("Hello suchi")
fun()


# In[20]:


def diff(x,y):
    result = x-y
    print("Difference of a & b is:", result)
x= 20
y= 10
diff(x,y)


# In[25]:


n= int(input())
m= int(input())
for num in range(n, m + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end = " ")


# In[33]:


a=int(input())
b=int(input())
if a>b or a<1 or b<1:
    print("Provide valid input")
else:
    while(a<=b):
        if a==2:
            print(a, end=" ")
        elif(a==1):
            a+=1
            continue
        else:
            flag=0
            for i in range(2,a//2+1):
                if a%i==0:
                    flag=1
                    break
            if flag==0:
                print(a,end=" ")
        a+=1  
    


# In[34]:


# X pattern
n= int(input("Enter the size:"))
val = n * 2 -1
for i in range(1, val+1):
    for j in range(1, val+1):
        if i==j or j==val-i +1:
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()


# In[36]:


# plus pattern
size = int(input("Enter the size:"))
for i in range(1,2*size):
    for j in range(1,2*size):
        if i==size or j==size:
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print()


# In[37]:


size = int(input("Enter the size:"))
for i in range(1,2*size):
    for j in range(1,2*size):
        if i==size or j==size:
            print('*',end=' ')                                                                                               
    print()


# In[3]:


n= int(input("Enter the size:"))
val=0
st=int(n/2+1)
if n%2!=0:
    for i in range(1,int(n/2+2)):
        for i in range(1,val+1):
            print(' ',end=' ')
    


# In[ ]:


var1='hi'
def abc():
    global var1
    var1 = 'Goodmorning'
    print(var1)


# In[ ]:


# program to demo acces of var in inner and outer functions
def outer_fun():
    var=11
        def inner_fun():
            var=22
            print("Outer variable:",var)
            print("Inner variable", var)
            


# In[2]:


#writing a function to understand mismatch parameers
def fun(i):
    print("orange",i)
fun(5+2*4)


# In[4]:


addition = lambda x,y,z:x+y+z
print("sum=", addition(10,20,30))


# In[6]:


addition = lambda x,y,z:x+y+z
print("sum=", addition(10,20,30))
'''
1. lambda fun have no names
2. It can take n no of attributes
3. It can only return 1 value
4. lambda fun cannot access global var
5. cannot access varother than their parameters list
6. cannot contain multi parameters
7. does not have explicit return stmts
'''


# In[7]:


#program to find smaller number by lambda
def small(a,b):
    if(a<b):
        return a
    else:
        return b
add = lambda x,y: x+y
diff = lambda x,y: x-y
print("smaller of 2 no:", small(add(-3,-2), diff(-1,-2)))


# In[8]:


def increment(y):
    return(lambda x : x+1)(y)
a=100
print("a=",a)
print("a after incrementing")
b= increment (a)
print(b)


# In[10]:


#program to pass lambda fun as a function args
def fun(f, n):
    print(f(n)) # twice(4)
twice = lambda x : x*2
triple = lambda x :x*3
fun(twice,4)
fun(triple,3)


# In[11]:


x= lambda : sum(range(1,11))
print(x())


# In[14]:


# swap using fun
def shifth(a,b):
    a,b=b,a
    print("after swap")
    print("a=",a)
    print("b=",b)
a=int(input("a="))
b=int(input("b="))
print("before swap")
print("a=",a)
print("b=",b)
shifth(a,b)


# In[15]:


'''
write a program to return full name of a person where first var passed is first name
second var passed is last name
'''
def name(fn,ln):
    s=' '
    n=fn+s+ln
    return n
print(name("Suchi","Lenkala"))     


# In[19]:


#write a program to calculate SI , suppose the customer is a senior citizen. he is being offered 12% ROI;
#for all other customers ,the ROI is 10%
p=100
r=3
SI = p*r*ROI/100
n= int(input()
for i in range(60):
    print(" ")
    


# In[23]:


def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
n= int(input())
print(fact(n))


# In[25]:


# program to find the exp(x,y) using recurssion function
def expo(x,y):
    if y==0:
        return 1
    else:
        return(x*expo(x,y-1))
n= int(input())
m= int(input())
print('result',expo(n,m))


# In[29]:


#fibonacci 
def fib(n):
    if n==0:
        return 0
    elif n<2:
        return 1
    return(fib(n-1)+fib(n-2))
n = int(input("Enter the range"))
for i in range(n):
    print("Finonacci(",i,")=",fib(i))


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
    


# In[ ]:


def fib(n):
    if n==0:
        return 0
    elif n<2:
        return 1
    return(fib(n-1)+fib(n-2))
n = int(input())
for i in range(n):
    print(fib(i))


# In[ ]:




