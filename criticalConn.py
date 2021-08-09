def criticalConn(connections):
  adj = [] * (len(connections)+1)
  for x in connections:
    u = x[0]
    v = x[1]
    print("u: {}, v: {}".format(u,v))
    adj[u].append(v)
    adj[v].append(u)
  
  
  return adj
  
  
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(criticalConn(connections))
