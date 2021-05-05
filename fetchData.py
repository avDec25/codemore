import requests

class ansItem:
  def __init__(self, title, cc):
    self.title = title
    self.cc = cc

  def __repr__(self):
    return "(Title={}, Comments={})\n".format(self.title, self.cc)



def fetchItems(limit):
  ansItems = []

  pageNumber = 1
  while 1:
    url = "https://jsonmock.hackerrank.com/api/articles?page={}".format(pageNumber)
    response = requests.get(url).json()
    
    if response["total"] == 0:
      break

    for item in response["data"]:
      if not item["title"] and not item["story_title"]:
        continue
      
      if not item["title"]:
        item["title"] = item["story_title"]
      
      if not item["story_title"]:
        item["story_title"] = item["title"]
      
      if not item["num_comments"]:
        item["num_comments"] = 0
      
      ansItems.append(ansItem(item["title"], item["num_comments"]))
      if len(ansItems) == limit:
        break

    if len(ansItems) == limit:
        break

    pageNumber = pageNumber + 1
    if pageNumber > response["total_pages"]:
      break

  ansItems.sort(key=lambda x:(x.cc, x.title))
  return ansItems

if __name__ == '__main__':
  limit = 490
  ans = fetchItems(limit)
  print(ans)
  print(len(ans))
