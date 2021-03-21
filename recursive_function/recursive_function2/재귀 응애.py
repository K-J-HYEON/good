def milkis(n, k):
    print('응애')
    if k==n:
        print(f'{k}번째 return')
        return
    else:
        print(k)
        milkis(n, k+1)
        print(f'{k}돌아온다')

milkis(3, 0)

