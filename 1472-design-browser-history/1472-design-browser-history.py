class BrowserHistory:

    def __init__(self, homepage: str):
        self.pos = 0
        self.max = 0
        self.url = [homepage]

    def visit(self, url: str) -> None:
        self.pos += 1
        self.max = self.pos 
        if self.pos >= len(self.url):
            self.url.append(url)
        else:
            self.url[self.pos] = url
        

    def back(self, steps: int) -> str:
        self.pos = max(0, self.pos - steps)
        return self.url[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = min(self.max, self.pos + steps)
        return self.url[self.pos]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)