# from collections import defaultdict

import collections
n, m = map(int, input().split())
dic = collections.defaultdict(int)
for _ in range(n):
    s, c = map(str, input().split())
    input_data = s+c
    dic[input_data] += 1
cnt = 0
for i, k in dic.items():
    if k < m:
        cnt += 1
    else:
        while k>0 :
            cnt += 1
            k-=m
print(cnt)



