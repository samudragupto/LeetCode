class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.curr + 1]
        self.history.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]
