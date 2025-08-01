from collections import deque

processes = ['P1', 'P2', 'P3', 'P4', 'P5']
arrival_time = [0, 1, 2, 3, 4]
burst_time = [5, 3, 1, 2, 3]
n = len(processes)
time_quantum = 2
remaining_time = burst_time[:]
waiting_time = [0] * n
turnaround_time = [0] * n
completion_time = [0] * n
visited = [False] * n
ready_queue = deque()

t = 0  
completed = 0

for i in range(n):
    if arrival_time[i] <= t and not visited[i]:
        ready_queue.append(i)
        visited[i] = True
while completed < n:
    if ready_queue:
        i = ready_queue.popleft()
        exec_time = min(time_quantum, remaining_time[i])
        t += exec_time
        remaining_time[i] -= exec_time
        for j in range(n):
            if arrival_time[j] <= t and not visited[j]:
                ready_queue.append(j)
                visited[j] = True

        if remaining_time[i] > 0:
            ready_queue.append(i)
        else:
            completion_time[i] = t
            turnaround_time[i] = completion_time[i] - arrival_time[i]
            waiting_time[i] = turnaround_time[i] - burst_time[i]
            completed += 1
    else:
        t += 1
        for i in range(n):
            if arrival_time[i] <= t and not visited[i]:
                ready_queue.append(i)
                visited[i] = True
print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")


