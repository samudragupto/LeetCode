class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0

        to_delete = []
        for t, expiry in self.tokens.items():
            if expiry > currentTime:
                count += 1
            else:
                to_delete.append(t)
        for t in to_delete:
            del self.tokens[t]
        return count
