# 조건문과 반복문, break를 활용하여 
# 다음 headlines 리스트의 요소들을 
# 130자 크기의 하나의 문자열로 이어 붙이는 코드를 작성하세요.
headlines = [
  "Local Bear Eaten by Man",
  "Legislature Announces New Laws",
  "Peasant Discovers Violence Inherent in System",
  "Cat Rescues Fireman Stuck in Tree",
  "Brave Knight Runs Away",
  "Papperbok Review: Totally Triffic"
]

# if문 / for문 break문 사용
# c = 1
# string = ''

# while 1:

# headlines = [
#   "Local Bear Eaten by Man",
#   "Legislature Announces New Laws",
#   "Peasant Discovers Violence Inherent in System",
#   "Cat Rescues Fireman Stuck in Tree",
#   "Brave Knight Runs Away",
#   "Papperbok Review: Totally Triffic"
# ]



# # index =0  # 맨 처음 index를 0으로 지정을 해주고
# # string = '' #string 변수에 빈값을 정해준다.
# # while 1: # while 1: 무한반복문으로 돌리고
# #     string += headlines[index] # string에 빈 값이 있었는데, headline의 index번째의 문자를 더해준다.
# #     index += 1 # index에 1씩 더해주고
# #     if index == len(headlines): # 만약에 index값이 headlines의 글자 수 값이면 
# #         break # 멈추고 
# # string = string.replace(' ','') #스트링의 ' '를 ''로 바꿔줘라(띄워써져 있는거를 ''로 바꿔줘라)
# # print(len(string)) #스트링의 글자 수를 출력해주고 #왜 글자 수가 163이 나오네?(130돼야 하는데)
# # print(string[:163]) #글자 수 출력 




total_str = '' # 빈 스트링 설정해주고
for i in range(len(headlines)): # 헤드라인스의 글자수 길이만큼 i 뽑아주고
    total_str += headlines[i] # total_str변수에 헤드라인스의 요소들을 하나씩 더해준다.
total_str=total_str.replace(" ", "") # " ",를 ""로 대체해주고


word_len130 = '' # word_len130 이라고 빈 값을 설정해주고  
for j in range(len(total_str)): # 토탈 스트링의 글자 길이 수 만큼 j를 뽑아주고
    word_len130 += total_str[j] # word_len130에다가 total_str의 j번째를 계속해서 더해주고
    if len(word_len130) == 130: # word_len130의 글자수가 130이라면
        print(word_len130) #그러면 word_len130을 출력해주고
        print(len(word_len130)) # hl의 글자 수도 뽑아주고
        break # 멈춰라



















# number = int(input('정수 입력:'))
# if number % 1 >= 1:
#     print("정수가 아닙니다.")

# elif number % 1 == 0:
#     print('정수 입니다.')

# else:
#     print('{}'.format('수가 아닙니다'))


# for i in range(10):
#     print(' {}번째 반복'.format(i))


# for i in range(1, 10):
#     print('{}번째 반복..1부터시작'.format(i))


# for i in range(1, 10, 2):
#     print("{}번째 반복.. 2증가됨".format(i)) 

# for i in 'a', 'b', 'c', 'd':
    # print('{} 문자열 반복'.format(i))

# 튜플형 반복
# for tup in (1, 2, 3, 4, 5, 6):
    # print('{} 튜플형 반복'.format(tup))


# dic = {1 : 'a', 2 : "b", 3 : "c"}
# for i in dic:
#     print('{}, {}'.format(i, dic[i]))

# what = [10, 35, 20, 3, 2, 9, 11]
# tmp = 0
# print('{}'.format(what))
# for i in range(len(what)):
#     for o in range(len(what)):
#         if what[i]<what[o]:
#             tmp=what[i]
#             what[i]=what[o]
#             what[0]=tmp
# print('{}'.format(what))

#while문
# x = 0
# while x in (0, 1, 2, 3):
#     x = x+1
#     print('while 반복문')

# y = 0
# while type(y) is int:
#     print('무한반복..{}번째 10번이 되면 break로 스탑'.format(y))
#     if y == 10:
#         break
#     y = y + 1

# 
