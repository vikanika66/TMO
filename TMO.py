
import math
import random
import numpy as np

lamb = 3
muu = 1

def lam (): 
    return -math.log(random.random())/lamb # Моделируем время прихода следующей заявки

def mu():
    return -math.log(random.random())/muu # Моделируем время обработки заявки


def model():
    
    t0 = 0 #время 0 
    channel = np.zeros(4) #зануляем каналы
    queque = [] #никого нет в очереди
    n = 0
    time = 0
    while t0 < 1000: 
        
        t0 +=  lam() #моделируем приход заявки
        
        while np.amin(channel) < t0 and len(queque) > 0: # Пока заявки не приходили приборы успели что-то обработать
    
            ch = np.argmin(channel) #найдем номер свободного канала
            n += 1
            time += channel[ch] - queque.pop(0)  #заявка обработалась, удалим ее
            channel[ch] += mu() #канал обрабатывает заявку
                
        if np.amin(channel) < t0: #
            n += 1 #если есть свободный канал, то обслуживаем заявку
            channel[np.argmin(channel)] = t0 + mu() #новое время обработки
        else:
            queque.append(t0) #нет свободных-добавим в очередь
    
    for a in queque: #неотработанные заявки 
        time += 1000 - a
        n += 1
    
    return time / n
    
    
    
    def main(): # Моделируем num_tests траекторий
    sum = 0
    i = 0
    while i < 1000:
        sum += model()#складываем все среднее время
        i+=1
    return sum/1000 #делим на количество траекторий
    
    
    print(main())
