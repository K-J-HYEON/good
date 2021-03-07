# from collections import Counter


# a = input()
# b = input()

# a_c = Counter(a)
# b_c = Counter(b)

# a_i_b = a_c & b_c

# # print(a_i_b)

# res = (a_c - a_i_b) + (b_c - a_i_b)

# print(sum(dict(res).values()))


from collections import Counter

a = input()
b = input()

a_c = Counter(a)
b_c = Counter(b)

a_i_b = a_c & b_c
print(a_i_b)

res = (a_c - a_i_b) + (b_c - a_i_b)

print(res)

print(sum(dict(res).values()))


