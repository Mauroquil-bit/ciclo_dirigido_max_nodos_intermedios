def dfs(graph, start, path, visited, all_cycles):
    path.append(start)
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, path, visited, all_cycles)
        elif neighbor in path:
            cycle_start_index = path.index(neighbor)
            cycle = path[cycle_start_index:] + [neighbor]
            all_cycles.append(cycle)

    path.pop()
    visited.remove(start)

def find_cycles(graph):
    all_cycles = []
    for node in graph:
        dfs(graph, node, [], set(), all_cycles)
    return all_cycles

def select_best_cycle(cycles):
    if cycles:
        # Seleccionar el ciclo con más nodos intermedios y el nodo inicial más pequeño
        max_cycle = max(cycles, key=lambda cycle: (len(cycle) - 1, -min(cycle)))
        return max_cycle
    return None

# Representación del grafo
graph = {
    1: [2],
    2: [3, 6],
    3: [],
    4: [1, 7],
    5: [1],
    6: [3, 7, 8],
    7: [5, 8],
    8: []
}

# Encontrar todos los ciclos
cycles = find_cycles(graph)

# Seleccionar el mejor ciclo
best_cycle = select_best_cycle(cycles)

if best_cycle:
    print("El mejor ciclo es:", best_cycle)
else:
    print("No se encontraron ciclos.")

