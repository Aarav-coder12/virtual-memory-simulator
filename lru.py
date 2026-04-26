class LRU:
    def __init__(self, frames):
        self.frames = frames
        self.memory = []
        self.page_faults = 0
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