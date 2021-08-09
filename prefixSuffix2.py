from typing import List


class WordFilter:
  mapOLargest = dict()

  def __init__(self, words: List[str]):
    for wi, w in enumerate(words):
      pfix = []
      sfix = []
      for i in range(len(w)):
        pfix.append(w[:i+1])
        sfix.append(w[-i:])
      
      for p in pfix:
        for s in sfix:
          key = p + "*" + s
          if key not in self.mapOLargest:
            self.mapOLargest[key] = wi
          else:
            self.mapOLargest[key] = max(self.mapOLargest.get(key), wi)
      
  def f(self, prefix: str, suffix: str) -> int:
    return self.mapOLargest.get(prefix + "*" + suffix)

  def printAllWords(self):
    for w in self.words:
      print(w)


wordFilter = WordFilter(["apple", "tapple", "mapple"])
print(wordFilter.f("t", "le"))
