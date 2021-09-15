#!/usr/bin/env python
# coding: utf-8

# In[4]:


def last(n):
    return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# In[30]:


ascii_dict = dict()
ascii_in_number = range(97,123)
for i in ascii_in_number:
    ascii_dict[(i)] = chr(i) 
print(ascii_dict)


# In[ ]:




