# AICA - Project - Comparition of BFS, DFS & A* Search Algorithm

## 1. Introduction

This Python project compares three pathfinding algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), and A* Search. They find paths through a grid containing obstacles. The project compares their path length, nodes visited, and execution time.

## 2. Features

* Implements BFS, DFS, and A* Search.
* Compares all three algorithms using the same destination.
* Allows users to select a destination.
* Detects walls and validates user input.
* Displays path length, nodes visited, and execution time.
* Provides options to run algorithms individually.

## 3. Technologies Used

* **Python 3** — Main programming language.
* **`collections.deque`** — Queue for BFS.
* **`heapq`** — Priority queue for A* Search.
* **`time`** — Measures execution time.
* **Lists and Dictionaries** — Store the grid and search information.

## 4. How It Works

1. The program uses a fixed 10 × 10 grid containing free cells and walls.
2. The user selects a destination using row and column coordinates.
3. The selected algorithm searches for a path from the starting point `(0, 0)`.
4. The program displays the path length, nodes visited, and execution time.
5. In comparison mode, all three algorithms run on the same destination, and their results are displayed in a table.

## 5. How to Run

**Requirements:** Python 3.

1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Run the Python file.
4. Select an option from the menu and enter the destination coordinates when prompted.

## 6. Limitations

The execution time may vary between runs, so predictions may not always be correct. It is intended for educational purposes only.


## 7. Future Improvements

* Add a graphical interface.
* Allow users to create obstacles and change the starting point.
* Visualize the search process and final path.
* Improve performance comparison using repeated trials.

## 8. Conclusion

This project demonstrates how BFS, DFS, and A* Search approach the same pathfinding problem differently. Comparing their results helps users understand search algorithms, data structures, and algorithm performance.
