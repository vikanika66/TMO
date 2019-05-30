import math
import random
import numpy as np

t_max = 1000
num_tests = 1000
input_par = 5
process_par = 1
num_channels = 6


#arr_devices.append(1)
#arr_devices.pop(0)

def sim_input ():
    return -math.log(random.random())/input_par

def sim_proc ():
    return -math.log(random.random())/process_par

def get_n_realiz(num_tests):
    sum = 0
    i=0
    while i < num_tests:
        sum+=simulate_func()
        i+=1
    return sum/num_tests

def simulate_func():
    
    t_now = 0
    arr_devices = np.zeros(num_channels)
    arr_queque = []
    result = {'processed' : 0, 'wait_time_total' : 0}
    
    while t_now < t_max:
        
        t_now +=  sim_input()
        while np.amin(arr_devices) < t_now and len(arr_queque) > 0:
            
            free_dev = np.argmin(arr_devices)
            
            result['processed'] += 1
            result['wait_time_total'] += arr_devices[free_dev] - arr_queque[0]
            
            arr_devices[free_dev] += sim_proc()
            arr_queque.pop(0)
            
        if np.amin(arr_devices) < t_now:
            result['processed'] += 1
            arr_devices[np.argmin(arr_devices)] += sim_proc()
        else:
            arr_queque.append(t_now)
    
    return result['wait_time_total']/result['processed']
    
print(get_n_realiz(num_tests))
