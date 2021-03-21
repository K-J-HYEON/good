# from itertools import combinations
# from collections import defaultdict
# def solutuion(orders, course):
#     orders = [sorted(i) for i in orders]
#     counter = defaultdict(int)
#     max_count = defaultdict(int)
#     for order in orders:
#         for c in course:
#             if len(order) < c:
#                 continue
#             # 단품메뉴의 모든 조합 확인
#             combination = combinations(order, c)
#             for each in combination:
#                 food = "".join(each)
#                 # 조합 등장횟수 + 1
#                 counter[food] += 1
#                 # 조합갯수별 최댓값 확인
#                 if max_count[c] < counter[food]:
#                     max_count[c] = counter[food]

#     answer = []
#     for c in course:
#         # 조합갯수의 등장횟수가 2보다 작을 경우 pass
#         if max_count[c] < 2: continue
#         answer += [i[0] for i in counter.items() if len(i[0]) == c and i[1] == max_count[c]]

#     return sorted(answer)


#=============================================================================

# course의 숫자 만큼 반복(2,3,5의 경우, 2개짜리 조합, 3개짜리 조합, 5개짜리 조합 찾기):
# 모든 order에 대해 반복:
# order에 대해 course 값(2개,3개,5개...) 만큼 조합/
# (orderr: A,B,C,F,G / course: 2 )의 경우 AB, AC, AF, AG, BC, BF...
# 'XY'와 'YX' 등의 경우를 위해 미리 정렬해준뒤 조합(예제 3번의 경우)
# 조합된 주문(메뉴 'A' + 메뉴 'Z' :'AZ') 에 대해 모든 주문 내역에 있는 해당 조합(ex.'AZ')의 갯수를Counter모듈을 이용하여 셈. 
# **해당 counter에 아무 값도 없거나(해당 주문 조합이 나온적이 없었거나), 최댓값이 1이면(해당 조합을 주문한 사람이 혼자라면) 패스
# **이 아니면 answer에 최댓값(현재 갯수에 해당하는 메뉴 조합 중 가장 많이 주문되었던 것) 을 가진 주문 조합을 다 넣는다.
 



from itertools import combinations #itertools에서 combinations매소드를 불러오고
from collections import Counter #collections에서 Counter매소드를 불러온다.


def solution(orders, course): #solution함수(orders와 course)를 호출해주고
    answer = [] # answer 빈 리스트를 만들어 주고
    for c in course: 
        temp = [] #temp 빈 리스트 만들어주고
        for order in orders: 
            combi = combinations(sorted(order), c) #order 오름차순 데로 정렬 후 =>오름차순된 order를 c번(ex)5C2) 조합 해준걸 combi에 저장
            temp += combi #temp에 combi저장
        counter = Counter(temp) #counter에 temp 리스트에 중복된 값까지 갯수 세어주는 Counter메소드 이용해서 저장
        if len(counter) != 0 and max(counter.values()) != 1: #counter 개수가 0이 아니고 counter의 최대값이 1이 아니면
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())] 
            # counter의 f번째 값이 최대값이면 =>  #f는 counter에서 뽑아와주고 join메소드 이용해서 구분해준다 = > answer에 저장

    return sorted(answer) # 오름차순된 answer 반환




# import itertools
# arr = ['A', 'B', 'C']
# nCr = itertools.combinations(arr, 2)
# print(list(nCr))
# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]



# collections.Counter 예제 (1)
# list를 입력값으로 함
# import collections
# lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']
# print(collections.Counter(lst))
# '''
# 결과
# Counter({'aa': 2, 'cc': 1, 'dd': 1, 'bb': 1, 'ee': 1})
