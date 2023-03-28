
# DFS 함수
def dfs(graph,v,visited):  
    visited[v] = True  #방문처리
    print(v,end=' ') #방문노드 출력
    
    for i in graph[v]: # 인접노드 순회
        if not visited[i]: # 방문이력 있는지 체크
            dfs(graph,i,visited) # 재귀호출
#Graph 자료구조        
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]    
]

#방문이력관리 배열
visited = [False]*9

#DFS 함수 호출
dfs(graph,1,visited)

