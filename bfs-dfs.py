from multiprocessing import Pool , Manager 

graph = {
    0 : [1,2],
    1 : [0,3,4],
    2 : [0,5],
    3 : [1],
    4 : [1,5],
    5 : [2,4]
}

def find_unvisited(data):
    current , visited = data
    return [ n for n in graph[current] if n not in visited]

def bfs(start):

    manager = Manager()
    visited = manager.list([start])
    queue = [start]

    while queue:

        print(queue, end =" ")

        with Pool() as pool:
            result = pool.map(find_unvisited,[(n,visited) for n in queue])

        new = []

        for r in result:
            for n in r:
                if n not in visited:
                    visited.append(n)
                    new.append(n)

        queue = new

def dfs(current,visited):
    if current not in visited:
        visited.append(current)
        print(current,end=" ")

        for n in graph[current]:
            dfs(n,visited)

if __name__ == "__main__":
    print("BFS : ")
    bfs(0)

    print("\nDFS : ")
    dfs(0,[])       