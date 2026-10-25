import time
import heapq
from collections import deque

# 0 = Free cell, 1 = Wall
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
]

start = (0, 0)
ROWS = len(grid)
COLS = len(grid[0])


def neighbors(cell):
    r, c = cell

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0:
            yield (nr, nc)


def build_path(parent, goal):
    path = []

    while goal is not None:
        path.append(goal)
        goal = parent[goal]

    return path[::-1]


# Breadth-First Search
def bfs(goal):
    queue = deque([start])
    parent = {start: None}
    visited = 0

    while queue:
        cell = queue.popleft()
        visited += 1

        if cell == goal:
            return build_path(parent, goal), visited

        for next_cell in neighbors(cell):
            if next_cell not in parent:
                parent[next_cell] = cell
                queue.append(next_cell)

    return None, visited


# Depth-First Search
def dfs(goal):
    stack = [start]
    parent = {start: None}
    visited = 0

    while stack:
        cell = stack.pop()
        visited += 1

        if cell == goal:
            return build_path(parent, goal), visited

        for next_cell in neighbors(cell):
            if next_cell not in parent:
                parent[next_cell] = cell
                stack.append(next_cell)

    return None, visited


# A* Search
def astar(goal):
    queue = [(0, start)]
    parent = {start: None}
    cost = {start: 0}
    visited = 0

    while queue:
        _, cell = heapq.heappop(queue)
        visited += 1

        if cell == goal:
            return build_path(parent, goal), visited

        for next_cell in neighbors(cell):
            new_cost = cost[cell] + 1

            if new_cost < cost.get(next_cell, float("inf")):
                cost[next_cell] = new_cost
                parent[next_cell] = cell

                distance = abs(next_cell[0] - goal[0]) + abs(next_cell[1] - goal[1])
                heapq.heappush(queue, (new_cost + distance, next_cell))

    return None, visited


algorithms = {
    "1": ("BFS", bfs),
    "2": ("DFS", dfs),
    "3": ("A* Search", astar)
}


def get_goal():
    while True:
        try:
            row = int(input("Enter destination row (0-9): "))
            col = int(input("Enter destination column (0-9): "))

            if 0 <= row < ROWS and 0 <= col < COLS:
                if grid[row][col] == 0:
                    return (row, col)

                print("That cell is a wall.")
            else:
                print("Enter numbers between 0 and 9.")

        except ValueError:
            print("Please enter whole numbers.")


def run_search(name, algorithm, goal):
    start_time = time.perf_counter()
    path, visited = algorithm(goal)
    elapsed = (time.perf_counter() - start_time) * 1_000_000

    steps = len(path) - 1 if path else "No path"

    return name, steps, visited, elapsed, path


def show_result(result):
    name, steps, visited, elapsed, path = result

    print("\nAlgorithm:", name)
    print("Path length:", steps, "steps" if path else "")
    print("Nodes visited:", visited)
    print(f"Execution time: {elapsed:.2f} microseconds")


def compare():
    goal = get_goal()
    results = []

    for name, algorithm in algorithms.values():
        results.append(run_search(name, algorithm, goal))

    print("\n--- ALGORITHM COMPARISON ---")
    print("Start:", start)
    print("Destination:", goal)
    print("-" * 55)
    print(f"{'Algorithm':<15}{'Steps':<12}{'Nodes':<12}{'Time (us)'}")
    print("-" * 55)

    for name, steps, visited, elapsed, path in results:
        print(f"{name:<15}{str(steps):<12}{visited:<12}{elapsed:.2f}")

    print("-" * 55)


def individual_search(choice):
    name, algorithm = algorithms[choice]

    print("\nSelected algorithm:", name)
    goal = get_goal()
    result = run_search(name, algorithm, goal)

    print("\nStart:", start)
    print("Destination:", goal)
    show_result(result)


while True:
    print("\n===== PATHFINDING SYSTEM =====")
    print("1. Compare All Algorithms")
    print("2. Search Using BFS")
    print("3. Search Using DFS")
    print("4. Search Using A* Search")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        compare()
    elif choice in ("2", "3", "4"):
        individual_search(str(int(choice) - 1))
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")