class Queue:
    FIFO = "FIFO"
    LIFO = "LIFO"
    STRATEGIES = [FIFO, LIFO]

    def __init__(self, strategy):
        if strategy not in self.STRATEGIES:
            raise ValueError(f' {strategy} is not in supported strategies {self.STRATEGIES}')
        self.storage = []
        self.strategy = strategy

    def add(self, value):
        self.storage.insert(0, value)

    def pop(self):
        if self.storage:
            if self.strategy == self.FIFO:
                return self.storage.pop()
            elif self.strategy == self.LIFO:
                return self.storage.append(0)
        return None
