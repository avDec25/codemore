import heapq

def genAllSubArrays(a):
  ans = []
  for i in range(len(a)+1):
    for j in range(i):
      ans.append(a[j:i])

  return ans

def generateOr(a):
  result = []
  for l in a:
    subRes = 0
    for e in l:
      subRes = subRes | e
    result.append(subRes)
  return result

givenList = [1, 2, 3]
k = 3
allSubArr = genAllSubArrays(givenList)
orList = generateOr(allSubArr)
print("allSubArr = {}".format(allSubArr))
print("orList = {}".format(orList))
heapq.heapify(orList)
print("smallest k from orList:")
while k > 0:
  print(heapq.heappop(orList))
  k -= 1

