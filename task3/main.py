import heapq

class Graph:
    def __init__(self):
        self.edges = {}  # Ключ - вершина, значення - список пар (сусідня вершина, вага ребра)

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        if to_vertex not in self.edges:
            self.edges[to_vertex] = []
        self.edges[from_vertex].append((to_vertex, weight))
        self.edges[to_vertex].append((from_vertex, weight))  # Якщо граф неорієнтований

    def dijkstra(self, start_vertex):
        # Ініціалізація відстаней та пріоритетної черги
        distances = {vertex: float('infinity') for vertex in self.edges}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]
        heapq.heapify(priority_queue)
        visited = set()

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Приклад використання

# Створюємо граф
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'E', 3)

# Виконуємо алгоритм Дейкстри від вершини 'A'
start_vertex = 'A'
distances = graph.dijkstra(start_vertex)

print(f"Відстані від вершини {start_vertex} до всіх інших вершин:")
for vertex, distance in distances.items():
    print(f"Відстань до вершини {vertex}: {distance}")
