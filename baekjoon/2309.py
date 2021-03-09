# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 
# 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 
# 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.

A = [] #A라는 빈 리스트에 값을 넣는다.
for i in range(9):
    A.append(int(input()))
A.sort() #값이 저장된 A 리스트를 오름차순으로 정렬한다.
result = sum(A) # 리스트에 있는 값들을 모두 더해서 9개의 수 중 2개를 뺐을 때, 
for i in range(9): #100이 돼야 하니, 리스트에 값들의 합에서 2개의 수를 뺀 값이
    for j in range(i+1, 9):#100이 된다면 그 수를 출력하도록 했다.
        if result-A[i]-A[j]==100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(A[k])
            exit()
