class TextEditor:
    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        for c in text:
            self.left.append(c)

    def deleteText(self, k: int) -> int:
        deleted = min(k, len(self.left))
        for _ in range(deleted):
            self.left.pop()
        return deleted

    def cursorLeft(self, k: int) -> str:
        moves = min(k, len(self.left))
        for _ in range(moves):
            self.right.append(self.left.pop())
        return "".join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        moves = min(k, len(self.right))
        for _ in range(moves):
            self.left.append(self.right.pop())
        return "".join(self.left[-10:])
