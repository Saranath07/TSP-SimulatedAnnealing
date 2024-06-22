# AI: Search Methods for Problem Solving - Programming Assignment 1



This code implements two algorithms for solving the Traveling Salesman Problem (TSP): Simulated Annealing (SA) combined with A* search and Dynamic Programming (DP). Here's a breakdown of the approach:

1. **Simulated Annealing (SA) with A\* Search:**
   - The SA algorithm is a probabilistic technique used for finding the global minimum in a large search space. It mimics the process of annealing in metallurgy, where a material is heated and then slowly cooled to decrease defects, thus minimizing energy. Similarly, SA explores the solution space by allowing "bad" moves early in the search with decreasing probability as the algorithm progresses.
   - A* search is a heuristic search algorithm that finds the least-cost path from a given initial node to one goal node. It uses a heuristic to estimate the cost of the cheapest path through any node. In this implementation, A* search is combined with SA to guide the search towards promising regions of the solution space.
2. **Dynamic Programming (DP):**
   - DP is a technique used for solving optimization problems by breaking them down into simpler subproblems and solving each subproblem only once, storing the solution to each subproblem to avoid redundant calculations.
   - The DP approach in this code iterates over all possible subsets of cities and calculates the shortest path for each subset. It utilizes memoization to store the solutions of subproblems and avoid recalculating them.
3. **Input Reading and Processing:**
   - The code first reads the type of graph (assuming it specifies the type of input data, such as Euclidean or Non-Euclidean) and the number of cities.
   - It then reads the input data as a distance matrix, representing the distances between pairs of cities.
4. **Solution Generation and Comparison:**
   - The code generates solutions using both SA with A* search and DP.
   - For SA with A* search, it runs the algorithm multiple times and selects the solution with the lowest cost.
   - If the number of cities is less than 19, it also calculates the optimal solution using DP and compares it with the solution obtained from SA with A* search. The optimal solution is printed if it has a lower cost; otherwise, the SA with A* search solution is printed.

Overall, the code provides a versatile approach to solving the TSP by combining two different algorithms and selecting the best solution based on the problem size.