from collections import deque

class FIFO:
    def __init__(self, frames):
        self.frames = frames
        self.memory = []
        self.page_faults = 0
        self.queue = deque()

    def access_page(self, page):
        if page not in self.memory:
            self.page_faults += 1
            if len(self.memory) < self.frames:
                self.memory.append(page)
                self.queue.append(page)
            else:
                removed = self.queue.popleft()
                self.memory.remove(removed)
                self.memory.append(page)
                self.queue.append(page)

        print(f"Page: {page} -> Memory: {self.memory}")

        # change 1