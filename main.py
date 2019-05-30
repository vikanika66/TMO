import math
import random
import numpy as np

t_max = 1000
num_tests = 1000
input_par = 5
process_par = 1
num_channels = 6


def sim_input ():
    return -math.log(random.random())/input_par # Моделируем время прихода следующей заявки

def sim_proc ():
    return -math.log(random.random())/process_par # Моделируем время обработки заявки

def get_n_realiz(num_tests): # Моделируем num_tests траекторий
    sum = 0
    i=0
    while i < num_tests:
        sum+=simulate_func()
        i+=1
    return sum/num_tests

def simulate_func():
    
    t_now = 0 # Начинаем в 0
    arr_devices = np.zeros(num_channels) # Создаем массив каналов
    arr_queque = [] # Очередь пустая
    result = {'processed' : 0, 'wait_time_total' : 0} # Результат пустой
    
    while t_now < t_max: # Пока не вышли за границы
        
        t_now +=  sim_input() # Текущее время - время прихода очередной заявки
        
        while np.amin(arr_devices) < t_now and len(arr_queque) > 0: # Пока заявки не приходили приборы успели что-то обработать
                                                                    # учтем это
            free_dev = np.argmin(arr_devices) # Номер свободного прибора
            
            result['processed'] += 1
            result['wait_time_total'] += arr_devices[free_dev] - arr_queque.pop(0)  # Добавим информацию об обработаной заявке 
                                                                                    # в результат и удалим ее из очереди
            arr_devices[free_dev] += sim_proc() # При назначении заявки на канал моделируем время обработки и запоминаем 
                                                # новое время освобождения канала
                
        if np.amin(arr_devices) < t_now: # Теперь разберемся с пришедшей заявкой
            result['processed'] += 1 # Если канал свободен, то ставим на обслуживание
            arr_devices[np.argmin(arr_devices)] = t_now + sim_proc() # Запоминаем новое время обработки
        else:
            arr_queque.append(t_now) # Если свободных нет, то добавляем в очередь
    
    for a in arr_queque: # Учтем время так и не обработанных заявок
        result['wait_time_total'] += t_max - a
        result['processed'] += 1
    
    return result['wait_time_total']/result['processed']
    
print(get_n_realiz(num_tests))
