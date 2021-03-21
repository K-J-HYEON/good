# 3단계
# 위의 유형은 DB관리 측면에서 굉장히 많이 출력된다. 예를 들면,  
# 리스트 안에 회원의 아이디, 회원가입날짜, 
# 사용자가 쓴 댓글들이 아래와 같이 구성되어 있다고 하자.

# 문제는 이런식이다. 각각의 DB의 회원들을 댓글들 중에 숫자를 제거하고, 
# 댓글들을 정렬한 후에, 가입한 날짜 순으로 재정렬하라. 
# 이러한 문제가 나왔다면 어떻게 풀 것인지 생각해보자. 
# 위의 방법을 모른다면 굉장히 복잡할 수 있는 문제지만,
# sort의 key를 적용한다면 쉽게 문제 풀이가 가능 할 것이다. 
# 힌트를 주자면 아래와 같이 str과 int를 분리가능하다.
data = ["hanpy 20101213 재미없다 235 재미있다", ...]

def divide_sentence(list_datas):
    str_I, int_I = [], []
    list_datas = list_datas.split()[2:]
    for data in list_datas:
        if data.isdigit():
            str_I.append(data)
        else:
            int_I.append(data)



divide_sentence(data)