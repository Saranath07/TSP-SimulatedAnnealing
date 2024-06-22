import time
import random
import math
import heapq



def TSP_SA_Astar(G):
 
    s = list(range(len(G)))
    c = cost(G, s)

   
    ntrial = 1
    T = 30
    alpha = 0.99

  
    open_set = [(c, s)]  
    # closed_set = set()

    while ntrial <= 100000:
       
        n = random.randint(0, len(G) - 1)
        while True:
            m = random.randint(0, len(G) - 1)
            if n != m:
                break
        s1 = swap(s, m, n)
        c1 = cost(G, s1)
        if c1 < c:
            s, c = s1, c1
        else:
            if random.random() < pow(math.e, -(c1 - c) / T):
                s, c = s1, c1

   
        if c1 < c:
            heapq.heappush(open_set, (c1, s1))

        if ntrial % 100 == 0:
            
            T = alpha * T

        ntrial += 1

    return s

def swap(s, m, n):
    i, j = min(m, n), max(m, n)
    s1 = s[:]
    while i < j:
        s1[i], s1[j] = s1[j], s1[i]
        i += 1
        j -= 1
    return s1

def cost(G, s):
    l = 0
    for i in range(len(s)-1):
        l += G[s[i]][s[i+1]]
    l += G[s[len(s)-1]][s[0]] 
    return l

def calculate_path_cost(distance_matrix, path):
  
    total_cost = 0
    number_of_cities = len(distance_matrix)

    
    for i in range(number_of_cities - 1):
        from_city = path[i]
        to_city = path[i + 1]
        total_cost += distance_matrix[from_city][to_city]

   
    total_cost += distance_matrix[path[-1]][path[0]]

    return total_cost





import math
from itertools import combinations

def TSP_DP(G):
    n = len(G)
    C = [[math.inf for _ in range(n)] for __ in range(1 << n)]
    C[1][0] = 0 
    P = [[() for _ in range(n)] for __ in range(1 << n)] 
    P[1][0] = (0,) 

   

    for size in range(1, n):
        for S in combinations(range(1, n), size):
            S = (0,) + S
            k = sum([1 << i for i in S])
            for i in S:
                if i == 0:
                    continue
                for j in S:
                    if j == i:
                        continue
                    cur_index = k ^ (1 << i)
                    if C[cur_index][j] + G[j][i] < C[k][i]:
                        C[k][i] = C[cur_index][j] + G[j][i]
                        P[k][i] = P[cur_index][j] + (i,)

    

    all_index = (1 << n) - 1
    path_costs = [(C[all_index][i] + G[0][i], P[all_index][i] + (0,)) for i in range(n)]
    min_path_cost, min_path = min(path_costs, key=lambda x: x[0])
    return min_path[:-1]



# Reading input
typeOfgraph = input().strip()
n = int(input().strip())

coordinates = []
for i in range(n):
    coordinates.append(tuple(map(float, input().strip().split())))

distance = []
for i in range(n):
    distance.append(list(map(float, input().strip().split())))


l1 = []
l2 = []
print(*TSP_SA_Astar(distance))
for i in range(70):
    l1.append(TSP_SA_Astar(distance))
    l2.append(calculate_path_cost(distance, l1[i]))
    min_cost = min(l2)
    min_cost_i = l2.index(min_cost)
    tsa_sol = l1[min_cost_i]
    print(*tsa_sol)






min_cost = min(l2)
min_cost_i = l2.index(min_cost)
tsa_sol = l1[min_cost_i]
print(*tsa_sol)
if n < 19:
    optimal_path_dp = TSP_DP(distance)
   

    if calculate_path_cost(distance, optimal_path_dp) < calculate_path_cost(distance, tsa_sol):
        print(*optimal_path_dp)
    else:
        print(*tsa_sol)
else:
    print(*tsa_sol)


