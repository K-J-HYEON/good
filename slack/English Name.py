# 예시 입력)
# Alice Betty Catherine Davis
# 예시 출력)
# Alice B. C. Davis


name = 'Alice Betty John Jason Catherine Davis' # 이름지정
N_l = name.split(' ') #' '단위로 나눠주고
c=0  # c = 0 으로 지정해놓고
for i in range(len(N_l)+1): # 네임길이만큼 i를 뽑아준다.
  c = c + i # c 초기값 0에다가 i를 더해주고
  avg = c / len(N_l) # c를 N_1만큼 나눠준다.=>avg이다


# avg
# print(avg)
import math # math를 임포트 해주고
a = math.floor(avg) # a값 : 내림하여 정수 반환
b = math.ceil(avg) #b값 : 올림하여 정수 반환
# print(a)
# print(b)
rName = ''  #rName 빈값으로 지정해놓고
for i in range(len(N_l)): # N_1-1 길이만큼 i 뽑아주고
  if i == a-1:  # 만약에 i가 a-1이면
    # print(f'{N_l[i][0]}.')
    rName += N_l[i][0]+'. ' # i번째의 0번째를 프린트하고
  elif i == b-1:
    # print(f'{N_l[i][0]}.')
    rName += N_l[i][0]+'. ' # i번째의 0번째를 프린트하고 
  else:
    # print(N_l[i]) # 아니면 다 프린트하라.
    rName += N_l[i]+' '
print(rName)

