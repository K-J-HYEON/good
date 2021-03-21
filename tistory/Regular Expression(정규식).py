# ^           라인의 처음을 매칭
# $            라인의 끝을 매칭
# .             임의의 문자를 매칭 
# \s          공백 문자를 매칭
# \S         공백이 아닌 문자를 매칭
# *            바로 앞선 문자에 적용되고 0 혹은 그 이상의 앞선 문자와 매칭을 표기함.
# *?          바로 앞선 문자에 적용되고 0 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.
# +           바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 표기함
# +?          바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.
# [aeiou]    명세된 집합 문자에 존재하는 단일 문자와 매칭. “a”, “e”, “i”, “o”, “u” 문자만 매칭되는 예제
# [a-z0-9]    - 기호로 문자 범위를 명세할 수 있다. 소문자이거나 숫자인 단일 문자만 매칭되는 예제.
# ( )         괄호가 정규표현식에 추가될 때, 매칭을 무시한다. 하지만 findall()을 사용 할 때 전체 문자열보다 매칭 된 문자열의 상세한 부속 문자열을 추출할 수 있게 한다.

# 정규식은 파이썬의 일부는 아니지만 함께 쓰인다. 관련 내용은 아래와 같다.

# import re
# 위와 같이 정규식 라이브러리를 가져와야 사용이 가능하다.

 

 

# 내장 함수로는 아래와 같다.

# re.search()는 매개 변수를 받아 문자열 내에서 검색을 해주는 함수이다.
# re.findall()는 문자열을 순회하면서 정해진 패턴을 만족하면 추출하는 함수이다.
 

# re.search()는 해당 문자열이 대상 정규식을 만족시키는지를 True/False로 리턴한다. 따라서 if문에서 사용하면 된다.

# 2.1. hanpy.text에서 From: 이 포함된 문자열을 찾아보자. 
# python함수를 사용
# content = open('hanpy.txt')
# for line in content:
#     line = line.rstrip()
#     if line.find('From:') >= 0:
#         print(line)


# re 사용
# content = open('hanpy.txt')
# for line in content:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)

#5.1find 사용 왜 31인지? / 5.2split사용 이해안됨 전체과정

# 2.2 hanpy.text에서 From: 이 처음에 포함된 문자열을 찾아보자. 
# python 함수 사용
content = open('hanpy.txt')
for line in content:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# re 사용
# content = open('hanpy.txt')
# for line in content:
#     line = line.rstrip()
#     if re.search('^From:', line):
#         print(line)
# 핵심은 From앞에 ^가 붙은 것을 확인할 수 있다. ^은 라인의 처음을
# 매칭 시키기 때문에 From:으로 시작한 line을 찾을 수 있다.

# ^X.*:
# ^ : X로 시작하는 것 찾기
# .* : 아무 문자나 여러 번 들어가기가 가능하다.
# :  : X로 시작하고 그 뒤에 :가 있는 단어가 있으면 선택한다는 말이다.

# ^X-\S+:
# 풀이해보면 X-로 시작한다.
# \S의 의미는 공백을 제외한 모든 것이 들어온다는 뜻이다. 
# + 의 의미는 한 번 이상 반복한다는 뜻이다.


 
