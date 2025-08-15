
processes = ['p1', 'p2', 'p3', 'p4', 'p5']
priority = [2, 0, 3, 1, 4]     
arrival = [0, 5, 12, 10, 16]
burst =   [11, 28, 2, 10, 16]

n = len(processes)

completion = [0] * n
turnaround = [0] * n
waiting = [0] * n
done = [False] * n

time = 0
completed = 0

while completed < n:
    idx = -1
    highest_priority = float('inf')
    for i in range(n):
        if not done[i] and arrival[i] <= time:
            if priority[i] < highest_priority:
                highest_priority = priority[i]
                idx = i

    if idx == -1:
        time += 1
        continue

   
    time += burst[idx]
    completion[idx] = time
    turnaround[idx] = completion[idx] - arrival[idx]
    waiting[idx] = turnaround[idx] - burst[idx]
    done[idx] = True
    completed += 1


print("Process\tAT\tBT\tPR\tCT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i]}\t{arrival[i]}\t{burst[i]}\t{priority[i]}\t{completion[i]}\t{turnaround[i]}\t{waiting[i]}")


