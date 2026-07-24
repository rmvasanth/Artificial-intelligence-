"""
Assessment 1 - Annexure A: Analytical Problem Solving
======================================================
Solves:
  1. Water Jug Problem (BFS over state space)
  2. Mars Rover agent description (printed analysis)
  3. 8-Queens Problem (backtracking search)
  4. OLA Cab utility-based agent (simulation)
  5. Uniform Cost Search on a delivery network graph
"""

import heapq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


# ---------------------------------------------------------------
# Q1: WATER JUG PROBLEM (BFS)
# ---------------------------------------------------------------
def water_jug_bfs(cap_a=4, cap_b=3, goal=2):
    start = (0, 0)
    frontier = deque([start])
    visited = {start}
    parent = {start: None}

    def neighbors(state):
        a, b = state
        yield (cap_a, b), "Fill 4-gal jug"
        yield (a, cap_b), "Fill 3-gal jug"
        yield (0, b), "Empty 4-gal jug"
        yield (a, 0), "Empty 3-gal jug"
        pour = min(a, cap_b - b)
        yield (a - pour, b + pour), "Pour 4-gal -> 3-gal"
        pour = min(b, cap_a - a)
        yield (a + pour, b - pour), "Pour 3-gal -> 4-gal"

    while frontier:
        state = frontier.popleft()
        if state[0] == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state][0] if parent[state] else None
            return list(reversed(path))
        for nxt, action in neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = (state, action)
                frontier.append(nxt)
    return None


# ---------------------------------------------------------------
# Q3: 8-QUEENS PROBLEM (Backtracking)
# ---------------------------------------------------------------
def solve_8_queens():
    n = 8
    cols = set()
    diag1 = set()
    diag2 = set()
    board = [-1] * n

    def backtrack(row):
        if row == n:
            return True
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            board[row] = col
            cols.add(col); diag1.add(row - col); diag2.add(row + col)
            if backtrack(row + 1):
                return True
            cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)
        return False

    backtrack(0)
    return board


def print_board(board):
    n = len(board)
    lines = []
    for r in range(n):
        row = ["Q" if board[r] == c else "." for c in range(n)]
        lines.append(" ".join(row))
    return "\n".join(lines)


# ---------------------------------------------------------------
# Q4: OLA CAB UTILITY-BASED AGENT (simulation)
# ---------------------------------------------------------------
def ola_cab_agent(available_cabs, weights=None):
    """
    available_cabs: list of dicts with keys fare, eta, comfort (1-5), seats
    Lower fare/eta = better. Higher comfort/seats = better.
    """
    if weights is None:
        weights = {"fare": -0.4, "eta": -0.2, "comfort": 0.3, "seats": 0.1}

    def utility(cab):
        return (weights["fare"] * cab["fare"] +
                weights["eta"] * cab["eta"] +
                weights["comfort"] * cab["comfort"] +
                weights["seats"] * cab["seats"])

    best = max(available_cabs, key=utility)
    ranked = sorted(available_cabs, key=utility, reverse=True)
    return best, ranked


# ---------------------------------------------------------------
# Q5: UNIFORM COST SEARCH on delivery network
# (Placeholder graph -- replace edges/weights with the actual
#  figure from your assignment if it differs)
# ---------------------------------------------------------------
GRAPH = {
    "S": {"A": 2, "C": 4},
    "A": {"B": 3, "D": 6},
    "B": {"D": 3, "G": 7},
    "C": {"D": 2},
    "D": {"G": 2},
    "G": {},
}


def uniform_cost_search(graph, start, goal):
    frontier = [(0, start, [start])]
    visited = {}
    explored_order = []

    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost
        explored_order.append((node, cost))

        if node == goal:
            return cost, path, explored_order

        for neighbor, edge_cost in graph.get(node, {}).items():
            new_cost = cost + edge_cost
            if neighbor not in visited or new_cost < visited.get(neighbor, float("inf")):
                heapq.heappush(frontier, (new_cost, neighbor, path + [neighbor]))

    return None, None, explored_order


def draw_graph(graph, path, filename):
    G = nx.DiGraph()
    for u, edges in graph.items():
        for v, w in edges.items():
            G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color="#cfe8ff", node_size=1200,
            font_weight="bold", arrowsize=20)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="#7CFC00")
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2.5)

    plt.title("UCS Least-Cost Path: S -> G")
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()


# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("Q1: WATER JUG PROBLEM")
    print("=" * 60)
    path = water_jug_bfs()
    for i, state in enumerate(path):
        print(f"Step {i}: (4-gal={state[0]}, 3-gal={state[1]})")

    print("\n" + "=" * 60)
    print("Q3: 8-QUEENS SOLUTION")
    print("=" * 60)
    board = solve_8_queens()
    print(print_board(board))
    print("Column positions per row:", board)

    print("\n" + "=" * 60)
    print("Q4: OLA CAB AGENT DECISION")
    print("=" * 60)
    cabs = [
        {"name": "Micro", "fare": 80, "eta": 5, "comfort": 2, "seats": 4},
        {"name": "Mini", "fare": 100, "eta": 4, "comfort": 3, "seats": 4},
        {"name": "Sedan", "fare": 150, "eta": 6, "comfort": 4, "seats": 4},
        {"name": "Prime", "fare": 220, "eta": 3, "comfort": 5, "seats": 4},
        {"name": "Shared", "fare": 50, "eta": 10, "comfort": 1, "seats": 1},
    ]
    best, ranked = ola_cab_agent(cabs)
    for cab in ranked:
        print(f"{cab['name']:8s} fare={cab['fare']:4d} eta={cab['eta']:2d} "
              f"comfort={cab['comfort']}")
    print(f"\nAgent selects: {best['name']}")

    print("\n" + "=" * 60)
    print("Q5: UNIFORM COST SEARCH (S -> G)")
    print("=" * 60)
    cost, path, order = uniform_cost_search(GRAPH, "S", "G")
    print("Expansion order (node, cumulative cost):")
    for node, c in order:
        print(f"  {node}: {c}")
    print(f"\nLeast-cost path: {' -> '.join(path)}")
    print(f"Total cost: {cost}")

    draw_graph(GRAPH, path, "Output.png")
    print("\nGraph with least-cost path saved to Output.png")
