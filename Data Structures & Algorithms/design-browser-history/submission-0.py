class BrowserHistory:
    def __init__(self, homepage: str):
        first_page = Website(homepage)
        self.head = first_page # first page ever, never moves
        self.current = first_page # where you are right now, moves around


    def visit(self, url: str) -> None:
        new_url = Website(url) 

        new_url.prev = self.current
        self.current.next = new_url

        self.current = new_url 
        self.tail = new_url


    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.url


    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url    
      
        
class Website:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

        