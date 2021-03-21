# .	줄 바꿈을 제외한 모든 문자
# ^	문자열의 시작
# $	문자열의 끝
# *	앞에 있는 문자가 0회 이상 반복된 문자열
# +	앞에 있는 문자가 1회 이상 반복된 문자열
# {m}	앞 문자를 m회 반복하는 문자열
# {m, n}	앞 문자를 m~n회 반목하는 문자열
# ?	앞 문자가 나오거나 나오지 않는 문자열({0,1}과 동일)
# \d	숫자
# \D	숫자가 아닌 문자
# \w	문자 혹은 숫자
# \W	문자 혹은 숫자가 아닌 것
# (...)	괄호 안의 모든 정규 표현식을 만족하는 문자
# [abc]	a, b, c 중 한 개의 문자와 일치

import re
# 2.1. re.compile( pattern )
# compile 함수는 특정 기호를 정규 표현식 객체로 만들어 준다. 
# re 라이브러리를 사용하려면 정규 표현식 패턴을 매번 작성해야 하지만, 
# compile을 사용하면 패턴을 필요할 때마다 사용할 수 있다.
pattern = '\W+'
re_pattern = re.compile(pattern)

re.search( "(\w+)", "wow, i love it!" )

re.split('\W', 'wow, it is world of word')

