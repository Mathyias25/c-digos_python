#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 08:32:41 2022
@author: Roberio Matias
Limites - Grings
"""
from sympy import *
init_printing()
x,y = symbols('x y')


# In[27]:


#=========AULA 01=====================
def f(x): return 2*x+1
f(x)
limit(f(x),x,1)
print(f(1))
#plot(f(x),(x,-5,5),ylim=(-10,10))


# In[38]:


def g(x): return (2*x+2)/(x+1)
g(x)
limit(g(x),x,3)
#plot(g(x),(x,-5,5),ylim=(-10,10))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[16]:


#=================AULA 09 ================
def f(x): return (sqrt(1+x)-sqrt(1-x))/x
print(f(x))
print(f(0.1))
limit(f(x),x,0)
#plot(f(x),(x,-5,5),ylim=(-1.5,1.5))


# In[ ]:




