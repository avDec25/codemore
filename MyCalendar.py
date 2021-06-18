import functools

class MyCalendar:
  events = []
  def __init__(self):
    self.events.clear()
    self.events = []

  def book(self, start: int, end: int) -> bool:
    if len(self.events) == 0:
      self.events.append((start, end))
      return True

    def compare(a, b):
      if a[0] == b[0]:
        return a[1] - b[1]
      else:
        return a[0] - b[0]

    def overlaps(a, b):
      ans = compare(a, b)
      if ans > 0:
        temp = a
        a = b
        b = temp
      return a[0] <= b[0] < a[1] or a[0] <= b[1] < a[1]

    for event in self.events:
      if overlaps(event, (start, end)):
        return False

    self.events.append((start, end))
    self.events = sorted(self.events, key=functools.cmp_to_key(compare))
    print(self.events)
    return True

obj = MyCalendar()
p1 = obj.book(10,20)
p2 = obj.book(15,25)
p3 = obj.book(20,30)
print(p1, p2, p3)
