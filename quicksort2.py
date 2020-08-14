import pandas as pd
import os
import time
import copy
import resource
import sys

sys.setrecursionlimit(1000010)

data = pd.read_csv('./data.csv', header=None)

print('[+] read data finished\n')

def quicksort(A):
    # if len(A) <= 1:
    #     return A
    pivot = A[0]
    small = []
    large = []
    for i in A[1:]:
        if i < pivot:
            small.append(i)
        else:
            large.append(i)

    if len(small) > 1:
        small = quicksort(small)
    if len(large) > 1:
        large = quicksort(large)

    return small + [pivot] + large
    

str_li = ['randomly arranged', 'sorted', 'reversed-sorted']
for i in range(3):
    pid = os.fork()

    if pid == 0:
        print('[*] quicksort for  [%19s ] START'%(str_li[i]))
        data_tmp = list(data.T[i])
        st = time.time()
        data_tmp = quicksort(data_tmp)
        # print(data_tmp[200:250])
        end = time.time()
        mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        print('[+] %13s: [%17.4f s ]'%('time consumed', end-st))
        print('[+] %13s: [%16d KB ]'%('memory used', mem))
        print('[*] quicksort for  [%19s ] END'%(str_li[i]))
        file_name = str(i+1)+'.csv'
        dataframe = pd.DataFrame(data_tmp)
        dataframe.to_csv(file_name, header=False, index=False)
        print('[+] %13s  [%19s ]\n'%('saved as', file_name))
        sys.stdout.flush()
        exit(0)
    else:
        os.wait()


# i = 1
# print('[*] quicksort for  [%19s ] START'%(str_li[i]))
# data_tmp = list(data.T[i])
# st = time.time()
# data_tmp = quicksort(data_tmp)
# # print(data_tmp[200:250])
# end = time.time()
# mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
# print('[+] %13s: [%17.4f s ]'%('time consumed', end-st))
# print('[+] %13s: [%16d KB ]'%('memory used', mem))
# print('[*] quicksort for  [%19s ] END'%(str_li[i]))
# file_name = str(i+1)+'.csv'
# dataframe = pd.DataFrame(data_tmp)
# dataframe.to_csv(file_name, header=False, index=False)
# print('[+] %13s  [%19s ]\n'%('saved as', file_name))
