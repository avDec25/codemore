from typing import List

class WordFilter:
  words = []
  
  def __init__(self, words: List[str]):
    self.words = words

  def f(self, prefix: str, suffix: str) -> int:
    prefixLen = len(prefix)
    suffixLen = len(suffix)
    largest = -1
    for i,w in enumerate(self.words):
      pfix = w[:prefixLen]
      sfix = w[-suffixLen:]
      if pfix == prefix and sfix == suffix:
        largest = max(largest, i)
      
    return largest
  
  def printAllWords(self):
    for w in self.words:
      print(w)


wordFilter = WordFilter(["apple", "tapple", "mapple"])
print(wordFilter.f("t", "le"))
