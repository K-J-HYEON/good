# 달력 출력하기
# 1월 1일 월요일부터 12월 31일까지 달력을 출력하세요.
# 예시 출력)
#     1 월
# Mo Tu We Th Fr Sa Su 
#  1 2 3 4 5 6 7 
#  8 9 10 11 12 13 14 
# 15 16 17 18 19 20 21 
# 22 23 24 25 26 27 28 
# 29 30 31 
#     2 월
# Mo Tu We Th Fr Sa Su 
#  1 2 3 4 5 6 7 
#  8 9 10 11 12 13 14 
# 15 16 17 18 19 20 21 
# 22 23 24 25 26 27 28 
#     3 월
# Mo Tu We Th Fr Sa Su 
#  1 2 3 4 5 6 7 
#  8 9 10 11 12 13 14 
# 15 16 17 18 19 20 21 
# 22 23 24 25 26 27 28 
# 29 30 31


# ...
# 정답


calendar = { 
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31,6: 30, 
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 
} 
weeks = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
for month, days in calendar.items():
  # print(month, days) #items를 이용해서

# a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
#>>> a.items()
# dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
  print(f'{month:10} 월')    #우측정렬 
  # print(f'{month:<10} 월') #좌측정렬
  # print(f'{month:^10} 월') #중앙정렬
  for w in weeks:
    print(f'{w}', end=" ")
  print('')
  for i in range(1, days+1):
    print(f'{i:2}', end=" ")
    if i % 7 == 0:
      print('')



# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for key, value in x.items():
#   print(key, value)





