processes = ['P1', 'P2', 'P3', 'P4']
arrival_time = [0, 1, 2, 3]
burst_time = [3, 2, 1, 4]
n = len(processes)

process_info = list(zip(processes, arrival_time, burst_time))

process_info.sort(key=lambda x: x[1])

completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

time = 0
for i in range(n):
    pid, at, bt = process_info[i]
    
    if time < at:
        time = at  
    
    time += bt
    completion_time[i] = time
    turnaround_time[i] = completion_time[i] - at
    waiting_time[i] = turnaround_time[i] - bt

print(f"{'Process':<8}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<6}{'WT':<5}")
for i in range(n):
    pid, at, bt = process_info[i]
    print(f"{pid:<8}{at:<5}{bt:<5}{completion_time[i]:<5}{turnaround_time[i]:<6}{waiting_time[i]:<5}")

