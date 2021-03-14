a, b = map(int, input().split())
if a != b:
    if a > b:
        a, b = b, a  #값 교환
    print(b-a-1)
    print(*range(a+1, b))
else:
    print(0)