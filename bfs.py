import sys 

def BFS(source, distance, graph): 
    visited = [False] * (n+1) 
    distance[source]=0
    queue = [] 
    queue.append(source) 
    visited[source] = True
    while len(queue)>0: 
        source = queue.pop(0)  
        for i in graph[source]: 
            if visited[i] == False: 
                queue.append(i) 
                visited[i] = True
                distance[i]=distance[source]+1

t=int(input())
for i in range(t):
    n=int(input())
    graph={}
    for i in range(n+1):
        graph[i]=[]
    distance1=[sys.maxsize]*(n+1)
    
    p=list(map(int, input().split()))
    for i in range(len(p)):
        if i<=n-1:
            graph[i].append(i+1)
        if (p[i]>=0 and i+p[i]<=n):
            graph[i].append(i+p[i])
        if (p[i]<0 and p[i]+i>=0):
            graph[i].append(i+p[i])

    BFS(0, distance1, graph)
    print(distance1[n])

  
