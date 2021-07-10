class Solution:
  def numberOfRounds(self, startTime: str, finishTime: str) -> int:
    startHour, startMin = startTime.split(":")
    finishHour, finishMin = finishTime.split(":")
    
    
    startHour = int(startHour)
    startMin = int(startMin)
    
    while startMin % 15 != 0:
      startMin += 1
      if startMin == 60:
        startMin = 0
        startHour += 1
        if startHour == 24:
          startHour = 0
    

    finishHour = int(finishHour)
    finishMin = int(finishMin)

    while finishMin % 15 != 0:
      finishMin -= 1
      if finishMin == 60:
        finishMin = 0
        finishHour -= 1
        if startHour == -1:
          startHour = 23

    ans = 0
    while True:
      if startHour == finishHour and startMin == finishMin:
        break
      print("==========================")
      print(f"\n{startHour}:{startMin}")
      print(f"\n{finishHour}:{finishMin}")
      print("==========================")
      ans += 1
      startMin += 15
      if startMin == 60:
        startMin = 0
        startHour += 1
        if startHour == 24:
          startHour = 0

    print(startHour, startMin)
    print(finishHour, finishMin)

    return ans

startTime = "20:00"
finishTime = "6:00"
Solution().numberOfRounds(startTime, finishTime)
