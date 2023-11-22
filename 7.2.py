import heapq

def least_reachable_city(n, edges, mileage):
    graph = {i: set() for i in range(n)}
    for u, v, w in edges:
        if w <= mileage:
            graph[u].add(v)
            graph[v].add(u)

    def num_reachable_neighbors(city):
        visited = set()
        def dfs(city):
            visited.add(city)
            for neighbor in graph[city]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(city)
        return len(visited)

    cities_neighbors = {num_reachable_neighbors(city): city for city in range(n)}
    min_reachable_city = cities_neighbors[min(cities_neighbors)]
    print(f"Наименее доступным городом является: {min_reachable_city}")
    print(f"Количество доступных соседей из {min_reachable_city}: {min(cities_neighbors)}")

n = 10
edges = [(1, 1, 10), (1, 6, 20), (0, 8, 15), (2, 4, 5)]
mileage = 50
least_reachable_city(n, edges, mileage)
