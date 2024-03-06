
n = int(input('number of visitors: '))

events = []
for _ in range(n):
    event_start, event_end = [int(i) for i in input().split()]
    events.append([event_start, 0])
    events.append([event_end, 1, 0])

events.sort(key= lambda element: element[0])

x = 0
most_visitors = 0
for event in events:
    if event[1] == 0:
        x += 1
    else:
        x -= 1
    most_visitors = max(most_visitors, x)

print(most_visitors)
