# def recursive_call(x):
#     print(x)
#     recursive_call(x+1)
    
# recursive_call(1)

# def function(k,n):
#     if n == k:
#         return
#     else:
#         function(k+1, n)

# function(0,2)

# # 1.1. 배열의 각 원소를 재귀 함수로 접근하기
A = [1, 2, 3]
def f(n, k):
    if n == k:
        print(A[k])
    else:
        f(n, k+1)
f(2, 0)




# 1.2. 재귀로 집합 A의 부분집합 만들기
def f(k, n):
    if n==k: # b배열을 벗어나면
        for i in range(n):
            if b[i] == 1:
                print(A[i], end='')
        print()
    else:
        b[k]=0
        f(k+1, n)
        b[k]=1
        f(k+1, n)

A = [1, 2, 3]
b = [0, 0, 0]
f(0, 3)



# 1.3. 부분집합 원소의 합
# 부분집합 배열 합의 최대값 구하기.
def f(k, n, s):
    global maxV
    if n==k:
        if maxV < s:
            maxV = s
    else:
        f(k+1, n, s+A[k])
        f(k+1, n, s)

maxV = 0
A = [1, 4, 3, 2]
f(0, 4, 0)
print(maxV)




# 1.4. 서로 다른 n개의 자연수의 집합에서 부분집합 원소의 합이 M인 경우가 몇 번인지 구하기
def f(k, n, s, M):
    global cnt
    if s==M:
        cnt+=1
        return
    elif n==k:
        return
    else:
        f(k+1, n, s+A[k], M)
        f(k+1, n, s, M)

A = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
cnt = 0
f(0, 10, 0, 42)
print(cnt)
