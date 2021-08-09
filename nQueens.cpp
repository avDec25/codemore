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


bool isValidPlacement(int b[5][5], int r, int c) {
  int i, j;

  for (j=0; j < c; ++j) {
    // cannot place the queen because some other queen already present
    if (b[r][j]) return false;
  }

  for (i=r, j = c; i >= 0 && j >=0; --i, --j) {
    if(b[i][j]) return false;
  }

  for(i=r, j=c; j>=0 && i < 5; ++i, --j) {
    if(b[i][j]) return false;
  }

  return true;
}


bool solve(int a[5][5], int c) {
  if(c >= 5) {
    return true;
  }

  for(int i=0; i < 5; ++i) {
    if (isValidPlacement(a, i, c)) {
      a[i][c] = 1;
      if(solve(a, c+1)) {
        return true;
      }
      a[i][c] = 0;
    }
  }

  return false;
}

int main()
{
  int board[5][5] = {
    {0, 0, 0, 0, 0 },
    {0, 0, 0, 0, 0 },
    {0, 0, 0, 0, 0 },
    {0, 0, 0, 0, 0 },
    {0, 0, 0, 0, 0 }
  };

  if(solve(board, 0)) {
    cout << "solution exists";
  } else {
    cout << "no solution";
  }
  cout << "\n";
  for (size_t i = 0; i < 5; i++) {
    for (size_t j = 0; j < 5; j++) {
      cout << board[i][j] << "\t";
    }
    cout << "\n";
  }
  
  return 0;
}