import pandas as pd
import os
import time
import copy
import resource
import sys

sys.setrecursionlimit(150000000)

data = pd.read_csv('./data.csv', header=None)

print('[+] read data finished\n')

def partition(A, l, h):
    small = []
    large = []
    pivot1 = A[l]
    pivot2 = A[h]

    for i in range(l+1,h+1):
        if A[i] < pivot:
            small.append(A[i])
        else:
            large.append(A[i])

    A = A[:l] + small + [pivot] + large + A[h:]

    return l + len(small)

def quicksort(A, l, h):
    if l < h:
        p = partition(A, l, h)
        if l < p - 1:
            quicksort(A, l, p - 1)
        if p + 1 < h:
            quicksort(A, p + 1, h)

str_li = ['randomly arranged', 'sorted', 'reversed-sorted']
for i in range(3):
    pid = os.fork()

    if pid == 0:
        print('[*] quicksort for  [%19s ] START'%(str_li[i]))
        data_tmp = list(data.T[i])
        st = time.time()
        quicksort(data_tmp, 0, len(data_tmp) - 1)
        end = time.time()
        mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        print('[+] %13s: [%17.4f s ]'%('time consumed', end-st))
        print('[+] %13s: [%16d KB ]'%('memory used', mem))
        print('[*] quicksort for  [%19s ] END'%(str_li[i]))
        file_name = str(i+1)+'.csv'
        dataframe = pd.DataFrame(data_tmp)
        dataframe.to_csv(file_name, header=False, index=False)
        print('[+] %13s  [%19s ]\n'%('saved as', file_name))
        break
    else:
        os.wait()
