#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'costsOfNodes' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY lines as parameter.
#

from collections import deque, defaultdict

def costsOfNodes(lines):    
    def install_package(package, dep_graph):
        dep_path = deque()

        if package not in dep_graph:
            return dep_path

        graph = defaultdict(list)
        in_degree = defaultdict(int)

        stack = [package]
        while stack:
            p = stack.pop()
            if p not in in_degree:
                in_degree[p] = 0
            if p not in graph:
                graph[p] = []
            if p in dep_graph:
                for child in dep_graph[p]:
                    in_degree[child] += 1
                    graph[p].append(child)
                    stack.append(child)

        sources = deque()
        for k,v in in_degree.items():
            if v == 0:
                sources.append(k)

        while sources:
            parent = sources.popleft()
            dep_path.appendleft(parent)
            for child in graph[parent]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        if len(dep_path) != len(graph):
            return []

        return list(dep_path)


    
    def createBuildGraph(lines):
        modules = defaultdict(list)
        for line in lines:
            data = line.split(',')
            row = list()
            for i in range(1, len(data)):
                row.append(data[i])
            modules[data[0]] = row
        return modules
    
    
    dep_graph = createBuildGraph(lines)
    ans = list()
    total = len(dep_graph.keys())
    for k in dep_graph.keys():
        print(f"{k}, {dep_graph[k]}")
        x = install_package(k, dep_graph)
        print(x)
        ans.append(f'{k},{total-len(x)}')
    return ans

lines = ['a,e,n,s', 's,h,n', 'e,n', 'h', 'n']
costsOfNodes(lines)