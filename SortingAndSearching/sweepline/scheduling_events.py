
n = int(input('num of events: '))

events = []
for _ in range(n):
    event_start, event_end = [int(i) for i in input().split()]
    events.append((event_start, event_end))

events.sort(key= lambda event: event[1])


selected_events = []
for event in events:
    if selected_events:
        if event[0] >= selected_events[-1][1]:
            selected_events.append(event)
    else:
        selected_events.append(event)

print(selected_events)
