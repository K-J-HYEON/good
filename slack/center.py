# --- # 정답을 적혀있습니다. 정렬 문제에서 활용될 알고리즘 입니다. 암기합시다
# # 정중앙
# 사용자가 입력한 문자열중 가운데 글자를 출력하세요.
# 단, 문자열이 짝수라면 가운데 두글자를 출력하세요.

# 예시 입력)
# abc
# 예시 출력)
# b


# text = input('문자열을 입력하시오.')
# center = len(text) // 2
# if len(text) % 2: #True  # 숫자가 0이면 False 1이면 True인 점을 이용해서 짧게 적은 것 

#     char = text[center]
# else:
#     char = text[center-1:center+1]
# print(char)







text = input('문자열을 입력하세요.')
cho = len(text)//2

if len(text)%2 :
    chocolate = text[cho]

else:
    chocolate = text[cho-1:cho+1]

print(chocolate)


















# text = input('문자열을 입력하시오.')
# center = len(text) // 2
# if len(text) % 2 == 1: 

#     char = text[center]
# else:
#     char = text[center-1:center+1]
# print(char)