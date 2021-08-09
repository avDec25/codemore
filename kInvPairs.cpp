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
ll MOD = 1000000000+7;
double eps = 1e-12;
 

class Solution {
  public:
    int kInversePairs(int n, int k) {
      vvi dp(n+1, vi(k+1,0));
      for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= k; j++) {
          if (j == 0)
            dp[i][j] = 1;
          else {
            for (int p = 0; p <= min(j, i - 1); p++) {
              dp[i][j] = (dp[i][j] + dp[i - 1][j - p]) % 1000000007;
            }
          }
        }
      }
      return dp[n][k];
    }
};

int main()
{
  int n = 1000, k = 1000;
  Solution solved;
  cout << solved.kInversePairs(n, k) << "\n";
  return 0;
}