def next_moves(position, grid):
    result=[]
    if position[0]-1>=0:
        if grid[position[0]-1][position[1]]==1:
            result.append((position[0]-1, position[1]))
    if position[0]+1<len(grid):
        if grid[position[0]+1][position[1]]==1:
            result.append((position[0]+1, position[1]))
    if position[1]-1>=0:
        if grid[position[0]][position[1]-1]==1:
            result.append((position[0], position[1]-1))
    if position[1]+1<len(grid[0]):
        if grid[position[0]][position[1]+1]==1:
            result.append((position[0], position[1]+1))
    return result
    

grid = [
    [0, 0, 0, 1, 1], # Row 0
    [0, 0, 0, 1, 1], # Row 1
    [1, 1, 1, 0, 0], # Row 2
    [1, 1, 1, 1, 0], # Row 3
    [0, 0, 0, 1, 0]  # Row 4
]

position_1 = (3, 2)
position_2 = (0, 4)
position_3 = (0, 1)

print(next_moves(position_1, grid))
print(next_moves(position_2, grid))
print(next_moves(position_3, grid))


def list_all_escape_routes(grid):
    


grid = [
    [1, 0, 1, 0, 1], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 0, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

print(list_all_escape_routes(grid))