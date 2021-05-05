#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>  
#include "pp.hpp"

using namespace std;
#define mp make_pair
#define pb push_back
#define INF 2e18
#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vector<int>> vvi;
typedef vector<vector<ll>> vvl;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<vector<pll>> vvpll;
ll MOD = 998244353;
double eps = 1e-12;

// vector<vector<int>> criticalConnections(int n, vector<vector<int>> &connections) {
void criticalConnections(int n, vector<vector<int>> &connections) {
  vvi adjList(n);
  for (int i = 0; i < connections.size(); ++i) {
    int u = connections[i][0];
    int v = connections[i][1];
    adjList[u].push_back(v);
    adjList[v].push_back(u);
  }

  cout << adjList << "\n";
  
}

int main()
{
  fast_cin();
  int n = 4;
  vvi connections = {
    {0, 1},
    {1, 2},
    {2, 0},
    {1, 3}
  };

  criticalConnections(n, connections);
  return 0;
}