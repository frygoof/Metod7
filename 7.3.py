import heapq

def least_reachable_city(n, edges, mileage):    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))        graph[v].append((u, w))
    def num_reachable_neighbors(city):
        heap = [(0, city)]        distances = set()
        while heap:
            curr_dist, neighbor = heapq.heappop(heap)
            if neighbor in distances:                continue
            if neighbor != city:
                distances.add(neighbor)                heap.extend((curr_dist + d, node) for node, d in graph[neighbor] if
                            node not in distances and curr_dist + d <= mileage)
        return len(distances)
    cities_neighbors = {num_reachable_neighbors(city): city for city in range(n)}    min_reachable_city = cities_neighbors[min(cities_neighbors)]
    print(f"Наименее доступным городом является: {min_reachable_city}")
    print(f"Количество доступных соседей из {min_reachable_city}: {min(cities_neighbors)}")
n = 10edges = [(1, 1, 10), (1, 6, 20), (0, 8, 15), (2, 4, 5)]
mileage = 50
least_reachable_city(n, edges, mileage)