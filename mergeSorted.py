def mergeSortedArrays(lists):
  ans = []
  indexes = [0] * len(lists)

  while True:
    gatherMin = []
    anyIncremented = False
    for i, a in enumerate(lists):
      print("i: {}, a: {}".format(i, a))
      if indexes[i] < len(a):
        anyIncremented = True
        gatherMin.append(a[indexes[i]])
        indexes[i] += 1
    if not anyIncremented:
      break
    else:
      gatherMin.sort()
      ans.extend(gatherMin)

  return ans


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(mergeSortedArrays(lists))
