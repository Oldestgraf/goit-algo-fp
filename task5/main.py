import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def list_to_heap_tree(arr):
    if not arr:
        return None

    def inner(index):
        if index >= len(arr):
            return None
        node = Node(arr[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner(0)

def rgb_color(step, max_steps):
    """Функція для генерації кольору залежно від кроку"""
    intensity = int(255 * (step / max_steps))
    return f'#{intensity:02x}{intensity:02x}{255 - intensity:02x}'

def dfs(tree_root):
    if tree_root is None:
        return
    stack = [tree_root]
    step = 0
    max_steps = count_nodes(tree_root)
    
    while stack:
        node = stack.pop()
        node.color = rgb_color(step, max_steps)
        draw_tree(tree_root)
        step += 1

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def bfs(tree_root):
    if tree_root is None:
        return
    queue = deque([tree_root])
    step = 0
    max_steps = count_nodes(tree_root)
    
    while queue:
        node = queue.popleft()
        node.color = rgb_color(step, max_steps)
        draw_tree(tree_root)
        step += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def count_nodes(node):
    """Підрахунок кількості вузлів у дереві"""
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# Приклад використання для перетворення списку в дерево купи і візуалізації обходу
heap_list = [0, 1, 2, 3, 4, 5, 6]
heap_tree_root = list_to_heap_tree(heap_list)

print("DFS traversal visualization:")
dfs(heap_tree_root)

# Перезапуск дерева для BFS
heap_tree_root = list_to_heap_tree(heap_list)

print("BFS traversal visualization:")
bfs(heap_tree_root)
