#!/usr/bin/env python
# coding: utf-8

# #### Задание 1

# In[ ]:


import numpy as np


# In[12]:


# Создаем массив 5x2

a = np.array([[1, 6],
              [2, 8], 
              [3, 10], 
              [3, 11], 
              [1, 7]])


# In[13]:


a


# In[20]:


#  Находим среднее значение

np.mean(a, axis = 0)


# In[22]:


mean_a = np.mean(a, axis = 0)


# In[23]:


mean_a


# #### Задание 2

# In[24]:


# Получение нового массива в результате вычитания двух других

a_centered = a - mean_a


# In[25]:


a_centered


# #### Задание 3

# In[27]:


# Умножение массива на скаляр

a_centered_sp = a_centered * 2


# In[28]:


a_centered_sp


# In[34]:


# Деление a_centered_sp на N-1 

c = a_centered_sp / (a.shape[0]-1)


# In[35]:


c


# #### Задание 4

# In[40]:


np.cov(a_centered_sp)[0,1]


# #### Задание 5

# In[41]:


import pandas as pd


# In[43]:


authors = pd.DataFrame({'author_id':[1, 2, 3],
                       'author_name':['Тургенев', 'Чехов', 'Островский']}, columns = ['author_id', 'author_name'])


# In[44]:


authors


# In[45]:


book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
                       'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 
                                     'Гроза', 'Таланты и поклонники'],
                    'price':[450, 300, 350, 500, 450, 370, 290]}, columns = ['author_id', 'book_title', 'price'])


# In[46]:


book


# In[48]:


authors.merge(book, how = 'left')


# In[52]:


autors_price = authors.merge(book, how = 'left')


# In[53]:


autors_price


# In[55]:


top5 = autors_price.nlargest(5, 'price')


# * Создайте датафрейм authors_stat на основе информации из authors_price.
# * В датафрейме authors_stat должны быть четыре столбца: author_name, min_price, max_price, mean_price, в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.

# In[129]:


# Максимальная цена
max_price = autors_price.groupby('author_name', as_index = False)['price'].max()
max_price.rename(columns={'price': 'max_price'}, inplace = True)
max_price


# In[134]:


# Минимальная цена
min_price = autors_price.groupby('author_name', as_index = False)['price'].min()
min_price.rename(columns={'price': 'min_price', 'author_name': 'author_name_1'}, inplace = True)
min_price


# In[135]:


# Средняя цена
mean_price = autors_price.groupby('author_name', as_index = False)['price'].mean()
mean_price.rename(columns={'price': 'mean_price', 'author_name': 'author_name_2'}, inplace = True)
mean_price


# In[136]:


authors_stat = pd.concat([max_price, min_price, mean_price], axis = 1, ignore_index=False)
authors_stat 


# In[138]:


authors_stat = authors_stat.drop(authors_stat.columns[[2, 4]], axis = 'columns')
authors_stat


# In[ ]:




