print("="*50)
print("      VIRTUAL MEMORY OPTIMIZATION SIMULATOR")
print("="*50)

from collections import deque

# ---------------- BASE CLASS ----------------
class MemorySimulator:
    def __init__(self, frames):
        self.frames = frames
        self.memory = []
        self.page_faults = 0

    def access_page(self, page):
        if page not in self.memory:
            self.page_faults += 1
            if len(self.memory) < self.frames:
                self.memory.append(page)
            else:
                self.replace_page(page)
        print(f"Page: {page} -> Memory: {self.memory}")

    def replace_page(self, page):
        pass


# ---------------- FIFO ----------------
class FIFO(MemorySimulator):
    def __init__(self, frames):
        super().__init__(frames)
        self.queue = deque()

    def replace_page(self, page):
        removed = self.queue.popleft()
        self.memory.remove(removed)
        self.memory.append(page)
        self.queue.append(page)

    def access_page(self, page):
        if page not in self.memory:
            self.page_faults += 1
            if len(self.memory) < self.frames:
                self.memory.append(page)
                self.queue.append(page)
            else:
                self.replace_page(page)
        print(f"Page: {page} -> Memory: {self.memory}")


# ---------------- LRU ----------------
class LRU(MemorySimulator):
    def __init__(self, frames):
        super().__init__(frames)
        self.recent = []

    def access_page(self, page):
        if page in self.memory:
            self.recent.remove(page)
            self.recent.append(page)
        else:
            self.page_faults += 1
            if len(self.memory) < self.frames:
                self.memory.append(page)
            else:
                lru = self.recent.pop(0)
                self.memory.remove(lru)
                self.memory.append(page)
            self.recent.append(page)

        print(f"Page: {page} -> Memory: {self.memory}")


# ---------------- FRAGMENTATION ----------------
def fragmentation(total_memory, used_memory):
    internal = total_memory - used_memory
    print("\nFragmentation Analysis")
    print(f"Total Memory: {total_memory}")
    print(f"Used Memory: {used_memory}")
    print(f"Internal Fragmentation: {internal}")


# ---------------- USER INPUT ----------------
def get_user_input():
    pages = list(map(int, input("\nEnter page reference string (space separated): ").split()))
    frames = int(input("Enter number of frames: "))
    return pages, frames


# ---------------- SIMULATION ----------------
def run_simulation():
    choice = input("\nUse default input? (y/n): ")

    if choice.lower() == 'y':
        pages = [7, 0, 1, 2, 0, 3, 0, 4]
        frames = 3
    else:
        pages, frames = get_user_input()

    print("\n--- FIFO Algorithm ---")
    fifo = FIFO(frames)
    for p in pages:
        fifo.access_page(p)
    print("Total Page Faults (FIFO):", fifo.page_faults)

    print("\n--- LRU Algorithm ---")
    lru = LRU(frames)
    for p in pages:
        lru.access_page(p)
    print("Total Page Faults (LRU):", lru.page_faults)

    fragmentation(100, 75)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    run_simulation()