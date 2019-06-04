#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import random
import numpy as np


# In[4]:


lam = 3
mu = 1


# In[5]:


def mod_lam (): #sim input
    return -math.log(random.random())/lam #приход заявки 


def mod_mu (): #sim proc
    return -math.log(random.random())/mu #обработка заявки 


# In[6]:


def proc():
    
    t0 = 0 # Начинаем в 0
    
    channels = np.zeros(4) #4 канала, заполняем 0
    ochered = [] #нет никого в очереди

    n = 0 #обработанные заявки 
    time = 0 #Общее время ожидания 
    
    while t0 < 1000: #до времени t=1000
        
        t0 +=  mod_lam() # Текущее время - время прихода очередной заявки
        
        while np.amin(channels) < t0 and len(ochered) > 0: # Пока заявки не приходили приборы успели что-то обработать
            free_dev = np.argmin(channels) # Номер свободного прибора
            n += 1
            time += channels[free_dev] - ochered.pop(0)  # Добавим информацию об обработаной заявке 
                                                                                    # в результат и удалим ее из очереди
            channels[free_dev] += mod_mu() # При назначении заявки на канал моделируем время обработки и запоминаем 
                                                # новое время освобождения канала
                
        if np.amin(channels) < t0: # Теперь разберемся с пришедшей заявкой
            n += 1 # Если канал свободен, то ставим на обслуживание
            channels[np.argmin(channels)] = t0 + mod_mu() # Запоминаем новое время обработки
        else:
            ochered.append(t0) # Если свободных нет, то добавляем в очередь
    
    for a in ochered: # Учтем время так и не обработанных заявок
        time += t0 - a
        n += 1
    
    return time/n


# In[7]:


def main(): # Моделируем num_tests траекторий
    sum = 0
    i=0
    while i < 1000:
        sum+=proc()
        i+=1
    return sum/1000


# In[8]:


print(main())


# In[ ]:




