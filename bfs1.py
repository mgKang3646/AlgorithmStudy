from collections import deque


def bfs(graph,start,visited):
    
    queue = deque([start])
    visited[start] = True
    
    while queue: #큐가 Empty 상태일때까지 반복
        pointer = queue.popleft()
        print(pointer, end=' ')

        for i in graph[pointer]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

visited = [False]*9

bfs(graph,1,visited)


