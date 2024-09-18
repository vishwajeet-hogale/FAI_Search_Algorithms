import heapq 
def return_matrix_mapping(x,y):
    m = {
        0 : "A",
        1 : "B",
        2 : "C",
        3 : "D"
    }
    return m[x] + str(y+1)
def h_func(goal_x,goal_y,st_x,st_y,n): 
    return round((abs(goal_x - st_x) + abs(goal_y - st_y)) / float(n - 1),2)
def a_star(graph,st_x,st_y,goal_x,goal_y):
    pq = []
    n = len(graph)
    heapq.heappush(pq, [h_func(st_x,st_y,goal_x,goal_y,n), 0, [st_x,st_y], [],[]])
    cnt = 2
    visited = [] 

    while pq:
        h, cost, current_node, path, path_embedded = heapq.heappop(pq)
        if current_node not in visited:
            visited.append(current_node)
            path_embedded = path_embedded + [return_matrix_mapping(current_node[0],current_node[1])]
            path = path + [current_node] 
            if current_node == [goal_x,goal_y]:
                return path 
            print("Step ",cnt)
            print()
            print("Current node : ",current_node)
            print("Neighbor costs \n" )
            neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
            for c1,c2 in neighbors:
                new_coordinate = [current_node[0] + c1*graph[current_node[0]][current_node[1]],current_node[1] + c2*graph[current_node[0]][current_node[1]]]
                # if new_coordinate == [goal_x,goal_y]:
                #     return path_embedded + [return_matrix_mapping(goal_x,goal_y)]
                if 0 <= new_coordinate[0] <= 3 and 0 <= new_coordinate[1] <= 3 :
                    g = cost + 1 + graph[current_node[0]][current_node[1]] # Doubt
                    print(return_matrix_mapping(new_coordinate[0],new_coordinate[1]), " : weight + cost = ", g)
                    heapq.heappush(pq, (g + h_func(goal_x,goal_y,new_coordinate[0],new_coordinate[1],n), g, new_coordinate, path,path_embedded))
            cnt += 1
            print("Priority Queue Status")
            print(pq)
            print()
    return None

if __name__ == "__main__":
    graph = [
    [2, 3, 2, 3],
    [1, 2, 1, 1],
    [3, 2, 2, 3],
    [1, 1, 3, "G"]
]
    
    print(a_star(graph,1,1,3,3))