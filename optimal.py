class Optimal:
    def __init__(self, frames, pages):
        self.frames = frames
        self.pages = pages
        self.memory = []
        self.page_faults = 0

    def run(self):
        for i, page in enumerate(self.pages):
            if page not in self.memory:
                self.page_faults += 1

                if len(self.memory) < self.frames:
                    self.memory.append(page)
                else:
                    future = self.pages[i+1:]
                    index_map = {}

                    for m in self.memory:
                        if m in future:
                            index_map[m] = future.index(m)
                        else:
                            index_map[m] = float('inf')

                    remove_page = max(index_map, key=index_map.get)
                    self.memory.remove(remove_page)
                    self.memory.append(page)

            print(f"Page: {page} -> Memory: {self.memory}")

            # update 3