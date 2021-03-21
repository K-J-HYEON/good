book_title = ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']
# 예시 출력)
# {'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}

#1. for와 if만 사용
#2. count()를 사용
#3. get() 사용

# # 1.
# a={}
# for k in book_title:
#        if k in a:
#             a[k] =  a[k] + 1  #a 안에 키값이 있으면 1씩 더한게 벨류고 
#        else:
#         a[k] = 1 #없으면 그냥 1 
# print(a)

# # 2.
# a={}
# for k in book_title:
#         a[k]=a.get(k,0) +1 #get(키, 기본값)
# print(a)

# # 3.
# a={}
# for k in book_title:
#         v = book_title.count(k)
#         a[k] = v
# print(a)


a = {}
for k in book_title:
        if k in a:
                a[k] = a[k]+1
        else:
                a[k] = 1

print(a)

a={}
for k in book_title:
        a[k]=a.get(k,0) +1
print(a)


a = {}
for k in book_title:
        v = book_title.count(k)
        a[k] = v
print(a)



























