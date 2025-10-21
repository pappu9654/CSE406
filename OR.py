from collections import deque

def round_robin(processes, quantum):
    n = len(processes)
    rem_bt = [bt for _, _, bt in processes]   
    t = 0  
    queue = deque()
    ct = [0] * n 
    visited = [False] * n
    gantt = []

   
    processes.sort(key=lambda x: x[1])

    queue.append(0)
    visited[0] = True

    while queue:
        i = queue.popleft()

       
        if rem_bt[i] > quantum:
            gantt.append((processes[i][0], t, t + quantum))
            t += quantum
            rem_bt[i] -= quantum
        else:
            gantt.append((processes[i][0], t, t + rem_bt[i]))
            t += rem_bt[i]
            rem_bt[i] = 0
            ct[i] = t  

       
        for j in range(n):
            if processes[j][1] <= t and not visited[j] and rem_bt[j] > 0:
                queue.append(j)
                visited[j] = True

       
        if rem_bt[i] > 0:
            queue.append(i)

    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    total_tat = total_wt = 0
    for i in range(n):
        pid, at, bt = processes[i]
        tat = ct[i] - at
        wt = tat - bt
        total_tat += tat
        total_wt += wt
        print(f"{pid}\t{at}\t{bt}\t{ct[i]}\t{tat}\t{wt}")

    print("\nGantt Chart:")
    for p, start, end in gantt:
        print(f"| {p} ({start}-{end}) ", end="")
    print("|")



processes = [
    ('P1', 0, 7),
    ('P2', 1, 4),
    ('P3', 2, 15),
    ('P4', 3, 11),
    ('P5', 4, 20),
    ('P6', 4, 9)
]
quantum = 4

round_robin(processes, quantum)