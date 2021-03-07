# def sum_digits(n):
#     if n < 10:
#         return n
#     return n % 10 + sum_digits(n // 10)

# print(sum_digits(22541))

def sum_digits(n):

    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


print(sum_digits(22541))



# 1 + 2254

# 4 + 225

# 5 + 22

# 2 + 2

# 2