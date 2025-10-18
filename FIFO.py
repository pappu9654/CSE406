def fifo_page_replacement(pages, capacity):
    memory = []  
    page_faults = 0

    print("Page\tMemory State")

    for page in pages:
        if page not in memory:
            if len(memory) == capacity:
                memory.pop(0)
            memory.append(page)
            page_faults += 1
        print(f"{page}\t{memory}")

    print("\nTotal Page Faults:", page_faults)
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 4

fifo_page_replacement(pages, capacity)
