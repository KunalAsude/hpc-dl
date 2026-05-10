from multiprocessing import Pool, Manager

graph = {}

def worker(data):

    node, visited = data

    return [n for n in graph[node]
            if n not in visited]


def bfs(start):

    manager = Manager()

    visited = manager.list([start])

    queue = [start]

    print("BFS Traversal:")

    while queue:

        print(queue, end=" ")

        with Pool() as pool:

            result = pool.map(
                worker,
                [(n, visited) for n in queue]
            )

        new = []

        for r in result:

            for n in r:

                if n not in visited:

                    visited.append(n)

                    new.append(n)

        queue = new


def dfs(node, visited):

    if node not in visited:

        visited.append(node)

        print(node, end=" ")

        for n in graph[node]:

            dfs(n, visited)


if __name__ == "__main__":

    nodes = int(input("Enter number of nodes: "))

    for i in range(nodes):

        neighbors = list(map(
            int,
            input(f"Enter neighbors of {i}: ").split()
        ))

        graph[i] = neighbors

    start = int(input("Enter starting node: "))

    bfs(start)

    print("\nDFS Traversal:")

    dfs(start, [])