
n = int(input('number of tasks: '))

tasks = []
for _ in range(n):
    duration, deadline = [int(i) for i in input().split()]
    tasks.append((duration, deadline))

tasks.sort(key=lambda task: task[0])

current_time = 0
selected_tasks = []
for task in tasks:
    if current_time <= task[1]:
        current_time += task[0]
        selected_tasks.append(task)
    
print(selected_tasks)