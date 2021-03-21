# 재귀
def factorial(n):
  if n == 0:
    return 1
  return factorial(n-1) * n
print(factorial(500))


# # 반복문
# def factorial(n):
#   result = 1
#   for i in range(1, n+1):
#     result = result = 1
#    return result
