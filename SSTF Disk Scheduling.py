

def sstf_disk_scheduling(requests, head):
    requests = requests[:]   
    seek_sequence = []
    seek_count = 0
    current_head = head

    print("Step | Current Head -> Next Request | Seek Distance")
    print("---------------------------------------------------")

    while requests:
   
        distances = {req: abs(current_head - req) for req in requests}
        next_request = min(distances, key=distances.get)
        distance = distances[next_request]

        seek_count += distance
        seek_sequence.append(next_request)

    
        print(f"{len(seek_sequence):>4} | {current_head:>12} -> {next_request:<13} | {distance}")

 
        current_head = next_request
        requests.remove(next_request)

    return seek_sequence, seek_count


requests = [176, 39, 114, 90, 26]
head = 60   

seek_sequence, total_seek = sstf_disk_scheduling(requests, head)

print("\nRequest sequence:", [176, 39, 114, 90, 26])
print("Head starts at:", head)
print("Seek sequence (SSTF):", seek_sequence)
print("Total seek operations:", total_seek)
