basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']


# f = 0
# n = 0
# for k in basket_items:
#     if k in fruits:
#         f+=basket_items[k]
#     elif k not in fruits:
#         n+=basket_items[k]
    

# print("과일은 {}개이고, {}개는 과일이 아닙니다.".format(f,n))


fru = 0
no_fru = 0
for k in basket_items:
    if k in fruits:
        fru+=basket_items[k]
    elif k not in fruits:
        no_fru+=basket_items[k]

print(f'과일은 {fru}개이고, {no_fru}개는 과일이 아닙니다.')

# fru = 0
# no_fru = 0
# for k in basket_items:
#     print(basket_items[k])
#     if k in fruits:
#         fru+=basket_items[k]
#     elif k not in fruits:
#         no_fru+=basket_items[k]

# print("과일은 {}개이고, {}개는 과일이 아닙니다.".format(fru, no_fru))








