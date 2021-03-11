# nums = []
# for i in range(7):
#     n = int(input())
# if n % 2 == 1:
#         nums.append(n)
# if len(nums) == 0:
#     print(-1)
# else:
#     print(sum(nums), min(nums), sep='\n')


# odd_nums = []
# for i in range(1, 7):
#     num = int(input())
#     if num % 2 == 1:
#         odd_nums.append(num)

# if len(odd_nums) == 0:
#     print(-1)

# else:
#     print(sum(odd_nums))

#     print(min(odd_nums))

import sys
input = sys.stdin.readline
s = []
for i in range(7):
    a = int(input())
    if a % 2 != 0: s.append(a)
if s:
    print(sum(s))
    print(min(s))
else:
    print(-1)