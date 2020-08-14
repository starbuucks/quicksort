import random
import pandas as pd
import copy

MAX = 30000

li = []
t = []

for i in range(MAX):
    t.append(random.randint(0,MAX))

print('[*] MAX : '+str(MAX))
li.append(t)
print('[+] random list created')
q = copy.deepcopy(t)
q.sort()
li.append(q)
print('[+] sorted list created')
r = copy.deepcopy(q)
r.reverse()
li.append(r)
print('[+] reversed sorted list created')

dataframe = pd.DataFrame(li)
dataframe.to_csv("data.csv", header=False, index=False)
print('[+] data.csv created')