class MinStack:

    def __init__(self):
        self.min_val = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_val and val <= self.min_val[-1]:
            self.min_val.append(val)
        elif not self.min_val:
            self.min_val.append(val)

    def pop(self) -> None:
        popped_val = self.stack.pop()
        if self.min_val and popped_val == self.min_val[-1]:
            self.min_val.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
