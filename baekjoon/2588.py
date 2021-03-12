#백준 2588
for i in range(0, 10):
        print(result.count(str(i)))

O = int(input())
H = input()

for i in range(0, 3): #이번에는 i를 0,1,2로 뽑아주고 
        print(O * int(H[2-i])) #H의 1의자리, 10의자리, 100의 자리 순으로 O와 곱해준다.
         
print(O*int(H))








# O = int(input()) #O는 int값으로 받아주고
# H = input() # H는 str으로 받아준다
# # list(H) # H를 리스트화 시킨다.

# for i in range(2, -1, -1): # 2,1,0번째 순으로 i를 뽑아준뒤
#     print(O * int(H[i])) #O와 H의 셋째 자리, 둘째 자리, 첫쨰자리 순으로 곱해준 값을 출력
# print(O * int(H)) # H를 int화 시켜주고 O와 곱해33준다.