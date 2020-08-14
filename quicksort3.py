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
    p1 = A[0]
    p2 = A[1]
    if p1 > p2:
        p1, p2 = p2, p1
    li1 = []
    li2 = []
    li3 = []
    for i in A[2:]:
        if i < p1:
            li1.append(i)
        else if i < p2:
            li2.append(i)
        else:
            li3.append(i)

    if len(li1) > 1:
        li1 = quicksort(li1)
    if len(li2) > 1:
        li2 = quicksort(li2)
    if len(li3) > 1:
        li3 = quicksort(li3)

    return li1 + [p1] + li2 + [p2] + li3
    

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
