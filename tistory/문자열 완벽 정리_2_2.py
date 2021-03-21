# 입력값 : ["eat","tea","tan","ate","nat","bat"]
# 출력값 : [["bat"],["nat","tan"],["ate","eat","tea"]]


# import collections
# data = ["eat","tea","tan","ate","nat","bat"]
# sort_data = collections.defaultdict(list)
# for word in data:
#     sort_data[''.join(sorted(word))].append(word)
# print(sort_data.values())

# def reverseString(str):
#     left_idx, right_idx = 0, len(str)-1
#     while left_idx < right_idx:
#         str[left_idx], str[right_idx] = str[right_idx], str[left_idx]
#         left_idx += 1
#         right_idx -= 1
#     print(str)


# a = ['a', 'b', 'c', 'd', 'e']
# reverseString(a)


def palindrome(n, left, right):
    while right <= len(data) and left >= 0 and data[left] == data[right-1]:
        right += 1
        left -= 1
    return data[left + 1 : right -1]

data = 'ewqpbewqbfjabcdefedcbaienqnfkndkl'
# data = 'abbc'
res = ''
if data == data[::-1] or len(data) < 2:
    print(data)
else:
    for i in range(len(data)-1):
        res = max(res, palindrome(len(data), i, i+1), palindrome(len(data), i, i+2), key=len)
    print(res)


