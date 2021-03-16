# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
# 1. visited (탐사 했는지 여부)
# 2. out (탐사 내용)
# 3. 재귀 함수 시
# - 탈출 조건 : Depth가 M일 때
# - 탐사를 안했을 경우 진행
# - Depth 탐색 전 : 탐사 시작(중복 제거), 탐사 내용 append
# - Depth 탐색 후 : 다음 탐사 준비, 탐사 내용 pop


N, M = map(int, input().split())
visited = [False] * N # 방문 여부check = > #False로 초기화된 list를 생성한다.
out = [] #출력 내용


# 0 3 1 부터 시작
def solve(depth, N, M):
    if depth == M: #탈출 조건
        print(' '.join(map(str, out))) #list를 str으로 합쳐 출력
        return
    for i in range(len(visited)): # 방문 check 하면서
        if not visited[i]: # 방문 안했다면
            visited[i] = True #방문 시작(중복제거)
            out.append(i+1) # 방문 내용
            solve(depth+1, N, M) # 깊이 우선 탐색
            visited[i] = False #깊이 방문 완료
            out.pop() # 방문 내용 제거

solve(0, N, M)

# solve(0, N, M)
# 0 3 1
# i = 0
# v[0] = true
# out = [1]
# 1 3 1
# 1 = 1
# out = 1
# v[0] = False
# out = []

# 0 3 1
# v[1] = True
# out = [2]
# 1 3 1
# 1 = 1
# out = 2
# v[1] = False
# out = []

# 0 3 1
# v[2] = True
# out = [3]
# 1 3 1
# 1 = 1
# out = 3
# v[2] = False
# out = []



