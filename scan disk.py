def scan_disk(requests, head, direction, disk_size=200):
    requests.sort()
    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]

    seek_sequence = []
    total_seek = 0
    current = head

    if direction == "left":
        
        for r in reversed(left):
            seek_sequence.append(r)
            total_seek += abs(current - r)
            current = r
        
       
        total_seek += current  
        seek_sequence.append(0)
        current = 0

        for r in right:
            seek_sequence.append(r)
            total_seek += abs(current - r)
            current = r
    else:
       
        for r in right:
            seek_sequence.append(r)
            total_seek += abs(current - r)
            current = r

       
        total_seek += (disk_size - 1 - current)
        seek_sequence.append(disk_size - 1)
        current = disk_size - 1

        for r in reversed(left):
            seek_sequence.append(r)
            total_seek += abs(current - r)
            current = r

    return total_seek, seek_sequence


requests = [14, 20, 29, 40, 50, 110]
head = 29
direction = "left"

seek_time, order = scan_disk(requests, head, direction)
print("Seek Sequence:", order)
print("Total Seek Time:", seek_time)
