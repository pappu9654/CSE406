
def fifo_page_replacement(pages, frame_count):
    frames = []
    page_faults = 0

    print("Page\tFrames\t\tPage Fault")
    print("---------------------------------")

    for page in pages:
        if page not in frames:
            page_faults += 1
            
            if len(frames) == frame_count:
                frames.pop(0)
            frames.append(page)
            fault_status = "Yes"
        else:
            fault_status = "No"

        print(f"{page}\t{frames}\t\t{fault_status}")

    print("---------------------------------")
    print(f"Total Page Faults = {page_faults}")


pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
frame_count = 3

fifo_page_replacement(pages, frame_count)