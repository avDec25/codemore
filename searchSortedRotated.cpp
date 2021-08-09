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

void indexOfKey(vi& a, int target) {
  int n = a.size();

  if (n == 0) {
    return -1;
  }

  int low = 0; int high = n-1;
  int first = a[0];
  while (low <= high) {
    int mid = low + (high-low)/2;
    
    int mid_value = a[mid];

    if (mid_value == target) {
      return mid;
    }

    bool mid_big = mid_value >= first;
    bool target_big = target >= first;

    if (mid_big == target_big) {
      if (mid_value < target) {
        low = mid+1;
      } else {
        high = mid-1;
      }
    } else {
      if (am_big) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
  }

  return -1;
}

int main()
{
  fast_cin();
  vi a = { 5,
           6,
           7,
           8,
           9,
           10,
           1,
           2,
           3 };

  int key = 3;

  cout << indexOfKey(a, 3) << "\n";

  return 0;
}