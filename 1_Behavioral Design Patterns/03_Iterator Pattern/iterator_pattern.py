"""
The iterator pattern allows you to traverse a collection without 
exposing its underlying representation. It's particularly useful 
when dealing with multiple data structures, as it provides a 
consistent interface for iteration, keeping the complexity 
hidden from the user.

"""



from typing import List, Any, Iterator

class BrowseHistory:
    def __init__(self):
        self._urls: List[str] = []

    def push(self, url: str):
        self._urls.append(url)

    def pop(self) -> str:
        return self._urls.pop()

    def create_iterator(self) -> Iterator:
        return BrowseHistoryIterator(self)

class BrowseHistoryIterator:
    def __init__(self, history: BrowseHistory):
        self._history = history
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self._index < len(self._history._urls):
            url = self._history._urls[self._index]
            self._index += 1
            return url
        raise StopIteration

# --- Client Code ---
if __name__ == "__main__":
    history = BrowseHistory()
    history.push("google.com")
    history.push("github.com")
    history.push("openai.com")

    for url in history.create_iterator():
        print(url)
