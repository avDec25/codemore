import re

exp = "-1/2+3-6/7*10-5"
allInts = map(int, re.findall("[+-]?\d+", exp))
print(list(allInts))
