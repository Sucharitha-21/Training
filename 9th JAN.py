#!/usr/bin/env python
# coding: utf-8

# In[2]:


size= int(input())
max = 0
count = 0
flag = 0
str=input()
arr=list(str)
for i in range(0,size):
    if arr[i]=='1':
        count= count+1;
        flag=1
    elif(arr[i]=='0' and flag==1):
        count=0
        flag=0
    if count>max:
        max=count
print(max)


# In[3]:


v=int(input())
w=int(input())
if w&1==1 or w<2 or w<=v:
    print("Invalid input")
else:
    x=((4*v)-w)//2
print("tw",x)
print("fw", v-x)


# In[7]:


#Binary tree
class bt:
    def __init__(self,  data):
        self.data= data
        self.lc = None
        self.rc = None
def insert(root, newvalue):
    if root is None:
        root= bt(newvalue)
        return root
    if newvalue<root.data:
            root.lc=insert(root.lc, newvalue)
    else:
            root.rc=insert(root.rc, newvalue)
    return root
def inorder(root):
    if root == None:
        return
    inorder(root.lc)
    print(root.data)
    inorder(root.rc)
root= insert(None, 15)
insert(root, 10)
insert(root, 24)
insert(root, 5)
insert(root, 14)
insert(root, 22)
insert(root, 55)
print("inorder traversal of a bst")
inorder(root)


# In[10]:


class Node:
    def __init__(self, key, l=None, r= None):
        self.key= key
        self.l= l
        self.r= r
def vot(node, dist, d):
    if node is None:
        return
    d.setdefault(dist,[]).append(node.key)
    vot(node.l, dist-1,d)
    vot(node.r, dist+1,d)
def pvot(root):
    d={}
    vot(root,0,d)
    for value in d.values():
        print(value)
if __name__=='__main__':
    root = Node(1)
    root.l= Node(2)
    root.r= Node(3)
    root.r.l= Node(4)
    root.r.r= Node(5)
    root.r.l.l= Node(6)
    root.r.l.r= Node(7)
    root.r.l.r.l= Node(8)
    root.r.l.r.r= Node(9)
pvot(root)


# In[ ]:


class Node:
    def __init__(self, key, 1=None, r= None):
        self.key= key
        self.l=1


# In[3]:


def segregateEvenOdd(arr):
    left,right = 0,len(arr)-1
    while left < right:
        while (arr[left]%2==0 and left < right):
            left += 1
        while (arr[right]%2 == 1 and left < right):
            right -= 1
        if (left < right):
              arr[left],arr[right] = arr[right],arr[left]
              left += 1
              right = right-1
arr = [10, 98, 3, 33, 12, 22, 21, 11]
segregateEvenOdd(arr)
#n= int(input("Enter the size:"))
print ("Array after segregation "),
for i in range(0,len(arr)):
    print (arr[i], end=" ")


# In[5]:


n=int(input("Enter size:"))
l=list(map(int,input().strip().split()))
m=[]
n=[]
for i in l:
    if(i%2==0):
        m.append(i)
    else:
        n.append(i)
c=m+n
print(*c,sep=" ")


# In[8]:


#write a program to combine list to a dictionary to form a hash table
#input : 
keys=['name', 'age', 'branch']
values=['ABC', '100', 'Aeronutical']
details= zip(keys, values)
Dict = dict(details)
print(Dict)


# In[ ]:


#write a program to store a sparse matrix into a dictionary
arr=[[0,0,0,1,0],
[2,0,0,0,3],
[0,0,0,4,0]]
dict={}
for i in range(len(arr)):
    print("\n")


# In[10]:


S= "suchi"
for i in S:
    c = 0
    for j in S:
        if i == j:
            c+=1
        if c > 1:
            break
    if c == 1:
        print(i)


# In[12]:


class Node:
    def _init_(self,num):
        self.num=num
        self.next=None
class llist:
    def _init_(self):
        self.head=None
    def push(self,newnum):
        newnode=Node(newnum)
        newnode.next=self.head
        self.head=newnode
    def insertnext(self,prenode,newnode):
        if prenode is None:
            print("The Previous Node")
            return
        newnode=Node(newnum)
        newnode.next=prenode.next
        prenode.next=newnode
    def append(self,newnum):
        newnode=Node(newnum)
        if self.head is None:
            self.head=newnode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newnode
    def printnum(self):
        t=self.head
        while(t):
            print(t.data)
            t=temp.next
if __name__=='__main__':
    l1=llist()
    l1.append(1)
    l1.append(3)
    l1.append(5)
    l1.append(8)
print(printnum)


# In[15]:


#Write a program to insert,delete a node in a single-linked list
#ex:1 3 5 8
class Node:
    def __init__(self,num):
        self.num=num
        self.next=None
class llist:
    def __init__(self):
        self.head=None
    def push(self,newnum):
        newnode=Node(newnum)
        newnode.next=self.head
        self.head=newnode
    def insertnext(self,prenode,newnode):
        if prenode is None:
            print("The Previous Node")
            return
        newnode=Node(newnum)
        newnode.next=prenode.next
        prenode.next=newnode
    def append(self,newnum):
        newnode=Node(newnum)
        if self.head is None:
            self.head=newnode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newnode
    def printnum(self):
        t=self.head
        while(t):
            print(t.data)
            t=temp.next
if __name__=='__main__':
    l1=llist()
    l1.append(1)
    l1.append(3)
    l1.append(5)
    l1.append(8)
print(printnum)


# In[ ]:




