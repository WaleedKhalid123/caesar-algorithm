#!/usr/bin/env python
# coding: utf-8

# In[25]:


def encrypt(txt,key):
    cipher_list = []
    for l in txt:
      position = ord(l)
    
      new_letter = chr(position+key) 
      
      cipher_list.append(new_letter)
    
    t = "".join(cipher_list)
    print(t)
    


# In[26]:


text = list(input("enter your text,please:"))
key = int(input("enter your key,please:"))
encrypt(text,key)

