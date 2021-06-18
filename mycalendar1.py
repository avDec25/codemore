class Node:
  def __init__(self, s, e):
    self.s = s
    self.e = e
    self.left = None
    self.right = None

class MyCalendar:
  def __init__(self):
    self.root = None
  
  def helper(self, start, end, node):
    if start >= node.e:
      if node.right:
        return self.helper(start, end, node.right)
      else:
        node.right = Node(start, end)
        return True

    elif end <= node.s:
      if node.left:
        return self.helper(start, end, node.left)
      else:
        node.left = Node(start, end)
        return True

    else:
      return False

  def book(self, start, end):
    if not self.root:
      self.root = Node(start, end)
      return True
    return self.helper(start, end, self.root)