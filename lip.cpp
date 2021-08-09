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
 
vvi directions = {
  {0, 1},
  {0, -1},
  {1, 0},
  {-1, 0}
};

int util(vvi& a, vvi& table, int H, int W, int i, int j) {
  if (table[i][j] > 0) {
    return table[i][j];
  }
  int mx = 0;
  for (int k=0; k < 4; ++k) {
    int x = i + directions[k][0];
    int y = j + directions[k][1];
    if ( x >= 0 && y >= 0 && x < H && y < W && a[x][y] > a[i][j] ) {
      int longest = util(a, table, H, W, x, y);
      mx = max(mx, longest);
    }
  }

  table[i][j] = 1 + mx;
  return table[i][j];
}

int lip(vvi& a) {
  int H = a.size();
  int W = a[0].size();
  int ans = 0;

  vector<vector<int>> table(H, vector<int>(W, 0));

  for (size_t i = 0; i < H; i++) {
    for (size_t j = 0; j < W; j++) {
      int longest = util(a, table, H, W, i, j);
      ans = max(longest, ans);
    }    
  }
  return ans;
}

int main()
{
  fast_cin();
  vvi matrix = {{9, 9, 4}, {6, 6, 8}, {2, 1, 1}};
  cout << lip(matrix) << "\n";  
  return 0;
}