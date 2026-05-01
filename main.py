import heapq

def dijkstra(graph, start):
    # Boshlang'ich qiymatlar
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Agar eski qiymat bo‘lsa, o'tkazib yuboramiz
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Agar yangi yo‘l qisqaroq bo‘lsa
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


# Graf (adjacency list ko‘rinishida)
graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
    'D': [('B', 1), ('C', 4), ('E', 3), ('F', 6)],
    'E': [('C', 8), ('D', 3)],
    'F': [('D', 6)]
}

start_node = 'A'
result = dijkstra(graph, start_node)

print("Eng qisqa masofalar:")
for node, dist in result.items():
    print(f"{start_node} -> {node} = {dist}")
