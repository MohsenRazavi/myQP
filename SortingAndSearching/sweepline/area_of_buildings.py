
n = int(input('number of buildings: '))

events = []
for _ in range(n):
    building_start, building_end, height = [int(i) for i in input().split()]
    events.append([building_start, 0, height])
    events.append([building_end, 1, height])

events.sort(key= lambda element: element[0])

max_height = 0
total_area = 0
start_location = 0
heights = [0]
for event in events:
    max_height = max(max_height, heights[-1])
    total_area += max_height * (event[0] - start_location)
    start_location = event[0]
    if event[1]: # end
        max_height = heights[-1]
    else: # start
        heights.append(event[2])

print(total_area)
    
