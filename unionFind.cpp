#include <bits/stdc++.h> 
#include "pp.hpp" 
using namespace std; 

unordered_map<int, int> parent;

void makeSet(vector<int> const &universe)
{
  for (int i: universe) {
    parent[i] = i;
  }
}
 

int Find(int k)
{
  if (parent[k] == k) {
    return k;
  } 
  return Find(parent[k]);
}
 
void Union(int a, int b)
{
  int x = Find(a);
  int y = Find(b); 
  parent[x] = y;
}

void solve(int n, vector<string>& qt, vector<int>& s1, vector<int>& s2) {  
  vector<int> p(n);
  for (int i=0; i<n; ++i) {
    makeSet(p);
  }
  
  for (int i=0; i < qt.size(); ++i)   { 
    int cand1 = s1[i]-1; int cand2 = s2[i]-1;
    if (qt[i] == "friend") { 
      Union(cand1, cand2); 
    } else { 
      int count = 0; int rc1 = Find(cand1); int rc2 = Find(cand2);
      for (int j = 0; j < n; ++j) { 
        int r = Find(j);
        if (r == rc1 || r == rc2) {
          ++count;
        } 
      }
      cout << count << "\n";
    } 
  } 
}

int main() {
  vector<string> qt = {"friend", "friend", "total"};
  vector<int> s1 = {1,2,1};
  vector<int> s2 = {2,3,4};

  solve(4, qt, s1, s2);

  return 0;
}