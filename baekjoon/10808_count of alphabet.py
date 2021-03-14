# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.

# my_word = list(str(input())) #리스트 형식으로 입력값 저장해주고 
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # 알파벳 나열 해준 다음(비효율적인거 같다,,)
# for i in range(len(alphabet)): #알파벳 길이만큼 i 뽑아 준 다음
#     y = my_word.count(alphabet[i]) #입력값에 각각의 알파벳이 몇 개가 있는지 세어주고
#     print(y, end=' ') # 갯수별로 프린트해준다.



k=input()
for i in range(26):
   res=chr(i+ord('a')) # 0 + ord('a') => 1 + ord('a') + 2 + ord('a') + --- 순서로 쭉
   print(k.count(res), end=' ')



# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for key, value in x.items():
#    print(key, value)
k = input()
for i in range(26):
   res=chr(i+ord('a'))
   print(k.count(res), end=' ')