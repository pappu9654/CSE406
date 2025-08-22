def fcfs_disk_scheduling(requests, head):
    seek_sequence = []
    seek_count = 0
    current_head = head

    print("Step | Current Head -> Next Request | Seek Distance")
    print("---------------------------------------------------")

    for i, req in enumerate(requests, start=1):
       distance = abs(current_head - req)
       seek_count += distance
       print(f"{i:>4} | {current_head:>12} -> {req:<13} | {distance}")
        
       seek_sequence.append(req)
    
       current_head = req

    return seek_sequence, seek_count

requests = [176, 39, 114, 90, 26]
head = 60  
seek_sequence, total_seek = fcfs_disk_scheduling(requests, head)

print("\nRequest sequence:", requests)
print("Head starts at:", head)
print("Seek sequence:", seek_sequence)
print("Total seek operations:", total_seek)
