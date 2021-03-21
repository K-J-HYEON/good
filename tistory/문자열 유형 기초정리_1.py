# 유형 1. 회문(Palindrome)
#  회문, 즉 팰린드롬이란 앞뒤가 똑같은 단어나 문장을 의미한다. 이때 대소문자를 구분하지 않으며 글자와 숫자만 따지면 된다. 
#  ex_ '가나다다나가' 'Madam, I'm Adam'

 

# 문제로는 "앞뒤가 같은 단어를 찾아라.", "회문인 것을 찾아라." 등으로 출제되며, 
# 최근 코딩 테스트는 영어로 코딩 테스트가 출제되고 있는데, 
# "Palindrome"이라는 단어나 직접적으로 나올 수 있으니 단어도 눈에 익혀두길 바란다. 파이썬으로 이해해 보면 아래와 같다.



def isPalindrome(str):
    for i in range(len(str)//2):
        if str[i] == str[-i-1]:
            continue
        else:
            print('회문이 아닙니다.')
    print('회문입니다.')

data = 'abcba'
isPalindrome(data)


def isPalindrome(str):
    for i in range(len(str)//2):
        if str[i] == str[-i-1]:
            continue
        else:
            print('회문이 아닙니다.')
    print('회문입니다.')


# 위의 예처럼 'abcba'과 같은 쉬운 회문은 쉽게 문제풀이가 가능하지만, 
# 'Madam, I'm Adam'와 같이 대소문자나 특수기호가 포함되어 있다면, 회문을 판별하기 전에 
# 'Madam, I'm Adam'에서 대문자와 특수기호를 제거하여, 'madamimadam'으로 변환해주는 
# 전처리 과정을 진행해 준 후에 판별을 진행한다.

# 1단계
# 첫 번째 풀이로는 문자열 매서드인 isalnum()과 lower()을 활용하여 
# 문자열을 리스트로 변환하여 문제를 풀어볼 것이다.

def inPalindrome(str):
    #전처리
    list_str = []
    for char in str:
        if char.isalnum():
            list_str.append(char.lower())
    
    # 회문 판별
    while len(list_str) > 1:
        if list_str.pop(0) != list_str.pop():
            print('회문이 아닙니다.')
            return
    print('회문입니다.')

a = 'OMadam, I\'m Adamo'
inPalindrome(a)


    
# 사실 위의 풀이는 쉽다고 느껴질 풀이다. 왜냐하면, 모든 알고리즘 풀이에서 리스트를 사용하여 
# 상대적으로 많이 쓰기 때문이다. 
# 하지만, python에서 append(), pop()와 같이 리스트의 크기를 변경하는 함수들을 사용하면 
# 굉장히 느려진다는 점을 초보단계에서는 일단 암기하고 넘어가자.

# 2단계
# 두 번째 풀이 단계는 슬라이싱이다. 
# [::-1]로 풀면 된다. [::-1]은 슬라이싱으로 문자를 뒤집어준다. 
# 따라서 '가나다다나가'를 회문인지를 판별하려면 아래와 같다.

s = ['가나다다나가']
if s == s[::-1]:
    print('회문이다')
    # 여기서는 대문자와 특수기호, 띄어쓰기를 제거하는 전처리 과정을 
    # 정규식(re)을 사용하여 진행할 것이다. 
    # 먼저 아래의 코드를 보자.


import re
def inPalindrome(str):
    # 대문자를 소문자로 변경
    str = str.lower()

    # 정규식 사용
    str = re.sub('[^a-z0-9]', '', str)
    if str == str[::-1]:
        print('회문입니다')
    else:
        print('회문이 아닙니다')

a = 'OMadam, I\'M AdamO'
inPalindrome(a)
'''
Omadamimadam0
'''


#3단계 pop()을 이용 리스트 안에 있는 1 제거
list = [1, 2, 3, 4, 5]
list.pop(0)
print(list)

#BFS(너비 우선 탐색??) Quene를 구현하기 위해서 deque를 사용한다.
# 현재 단계에서는 BFS, DFS니 알 필요는 없고, 리스트의 append와 pop 대신에 
# deque를 이용한다는 정도만 알아두자. 
# 천천히 정리해서 하나씩 올려 보겠다. 코드를 보자.

import collections
def inPalindrome(str):
    deq = collections.deque()
    for char in str:
        if char.isalnum(): # 영문자, 숫자 여부를 판별하여, 영문자와 숫자가 아니면 False를 리턴한다.
            deq.append(char.lower())

    # 회문 판별
    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            print('회문이 아닙니다.')
            return
    print('회문입니다.')

a = 'OMadam, I\'m AdamO'
inPalindrome(a)





# deq의 사용법은 list와 비슷하다. append, pop를 동일하게 사용하면 된다. 
# 다만, pop(0) 대신에 popleft()를 사용한다. pop(0)과 popleft의 성능을 비교하면, 
# pop(0)은 전체 리스트의 원소를 하나씩 확인하여 찾는 반면에 
# popleft는 한 번에 찾기 때문에 빠르다.

# 유형 2. 문자열 뒤집기
# 이 유형은 리스트 내부에 있는 문자열을 뒤집는 방법을 물어보는 것이다. 
# 예를 들면 ['a', 'b', 'c']를 ['c', 'b', 'a']로 변환하는 방식을 물어보는 것이다.
 
# 1단계 reverse()함수
def reverseString(str):
    str.reverse()
    print(str)

a = ['a', 'b', 'c', 'd', 'e']
reverseString(a)


# 2단계
# 우리는 위에서 [::1]라는 슬라이싱을 배웠다. 
# 슬라이싱은 문자열뿐만 아니라, 리스트에서도 사용 가능하다.

a = 'abcde'
a = a[::-1]
print(a)

a = ['a', 'b', 'c', 'd', 'e']
a = a[::-1]
print(a)

# 3단계
# 투 포인터를 이용한 방법에 대해 알아보자. 
# 아래의 코드처럼 처음과 끝은 인덱스를 변수로 지정한 후에 변수를 
# +1이나 -1 하여 인덱스를 이동시켜 조작하는 방식이다. 
# 포인터를 활용한 방식은 나중에 정렬을 배울 때도 
# 유용하게 사용되므로 이해하고 넘어가자.

def reverseString(str):
    left_idx, right_idx = 0, len(str)-1
    while left_idx < right_idx:
        str[left_idx], str[right_idx] = str[right_idx], str[left_idx]
        left_idx += 1
        right_idx -=1
    print(str)

a = ['a', 'b', 'c', 'd', 'e']
reverseString(a)






# 번호 순 정렬이 아닌 그 뒤의 문자 순으로 정렬을 해보자
# 자주 출제가 되니 암기
data = ['1 A', '1 B', '6 A', '2 D', '4 B']

def func(x):
    return x.split()[1], x.split()[0] 
data.sort(key=func)
print(data)




data = ['1 A', '1 B', '6 A', '2 D', '4 B']
data.sort(key = lambda x: (x.split()[1], x.split()[0]))
print(data)




data = ['1 A', '1 B', '6 A', '2 D', '4 B']
def func(x):
    return x.split()[1], x.split()[0]

data.sort(key=func)
print(data)

data.sort(key = lambda x: (x.split()[1], x.split()[0]))