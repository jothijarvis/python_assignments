#  author: Jothiswarooban k
import time
# def functionexample():
#     print('Helo user')
def decoratorlogfunc(functionpointer):
    def insidelogfunction(*args,**kwds):

        log_file = open("D:/pytraining/Assignment1/decorators_logfile.txt","w")
        log_file.write("Function started to log data\n")          
        print('function started')
        f = functionpointer(*args,**kwds)
        print('function terminated')
        log_file.write("Function Terminated  log of data\n")      
        log_file.close() 
        return f
    return insidelogfunction

def decoratorfunc(functionpointer):
    def insidefunction(*args,**kwds):
        # add timer starting here
        start_time = time.perf_counter()
        f = functionpointer(*args,**kwds)
        # add timer end here
        end_time = time.perf_counter()
        total_duration = end_time-start_time
        print('time taken',total_duration)
        return f
    return insidefunction

@decoratorlogfunc
@decoratorfunc
def average(*args):
    '''stream in int values to get average'''
    if len(args) > 0:
        int_avg = sum(args)/len(args)
        print('avg value',int_avg)
        return int_avg
    else :
        return 0

# average_calc(1,2,3,4,5,8,6)
c = average(1, 2, 3, 29, -10) + average(1, 2)
print(c)

