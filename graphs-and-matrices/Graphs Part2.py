def can_rebook(flights, source, dest):
    queue=[]
    visited=set()
    queue.append(source)
    while queue:
        current=queue.pop(0)
        if current==dest:
            return True
        i=0
        for neighbor in flights[current]:
            if neighbor==1 and i not in visited:
                visited.add(i)
                queue.append(i)
            i=i+1
    return False

flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2)) 