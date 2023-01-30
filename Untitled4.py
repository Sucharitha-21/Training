#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#generate all permutations of a list in python
def perm(start,end=[]):
    if(len(start)==0):
        print(end)
    else:
        for i in range(len(start)):
            perm(start[:1]+start[i+1:],end+start[i:i+1])
perm([1,2,3])


# In[ ]:


'''
1) Factorial of a number
2) Fibonacci series
3) prime or not
4) write a python program to remove an empty tuples from a list
5) To calculate the average of elements in a list
6) write a python program to print spcified list after removing the 0th, 4th, 5th elements
   sample list:['Red','Green','White','Black','Pink','Yellow']
   Expected op:['Green','White','Black']
7) Write a python program to generate all permutations of a list in python
8) Write a python program to calculte the product, multiplying all the nubers of a givn tuple
9) counting repeated characters in a string
10) Reverse a string if its length is a multiple of 4
11) To separate even, odd and zero from a list
12) Split a given dictonary of lists into list of dictionaries
'''

