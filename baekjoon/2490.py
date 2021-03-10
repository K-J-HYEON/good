# #윷놀이

# lists = [0]*4
# for i in range(3):
#     lists = list(map(int,input().split()))
#     if lists.count(1) == 0:
#         print('D')
#     elif lists.count(1) == 1:
#         print('C')
#     elif lists.count(1) == 2:
#         print('B')
#     elif lists.count(1) == 3:
#         print('A')
#     elif lists.count(1) == 4:
#         print('E')

yut = [sum(list(map(int, input().split()))) for _ in range(3)]

for score in yut:
    if score == 0:
        print('D')
    elif score == 1:
        print('C')
    elif score == 2:
        print('B')
    elif score == 3:
        print('A')
    elif score == 4:
        print('E')