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
 

int solve(vvi& a){
  int H = a.size();
  int W = a[0].size();
  
  int ans = 0;

  vvi dp(H, vi(W));
  
  for (size_t i = 0; i < H; i++) {
    for (size_t j = 0; j < W; j++) {
      if(a[i][j] == 1) {
        if( i == 0 || j == 0) {
          dp[i][j] = 1;
        } else {
          dp[i][j] = 1 + min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
        }
        ans = max(ans, dp[i][j]);
      }
    }
  }
  
  return ans * ans;
}

int main()
{
  fast_cin();
  ll r; cin >> r;
  ll c; cin >> c;
  vvi a(r, vector<int>(c));
  for (size_t i = 0; i < r; i++) {
    for (size_t j = 0; j < c; j++) {
      cin >> a[i][j];
    }
  }
  cout  << solve(a) << "\n";
  return 0;
}