processes = ['P1', 'P2', 'P3', 'P4']
arrival_time = [0, 1, 2, 3]
burst_time = [3, 2, 1, 4]
n = len(processes)

process_info = list(zip(processes, arrival_time, burst_time))
completed = []
time = 0

completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

while len(completed) < n:
 
    ready_queue = [p for p in process_info if p[1] <= time and p[0] not in completed]
    
    if not ready_queue:
        time += 1  
        continue

    shortest = min(ready_queue, key=lambda x: x[2])
    
    pid = shortest[0]
    at = shortest[1]
    bt = shortest[2]
    
    index = processes.index(pid)
    
    time += bt
    completion_time[index] = time
    turnaround_time[index] = completion_time[index] - at
    waiting_time[index] = turnaround_time[index] - bt
    
    completed.append(pid)


print(f"{'Process':<8}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<6}{'WT':<5}")
for i in range(n):
    print(f"{processes[i]:<8}{arrival_time[i]:<5}{burst_time[i]:<5}{completion_time[i]:<5}{turnaround_time[i]:<6}{waiting_time[i]:<5}")

