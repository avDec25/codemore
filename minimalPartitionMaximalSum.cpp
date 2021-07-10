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

static void findSubset(vector<int> arr)
{
	int N = arr.size();
	map<int,int> mp;
	int totSum = 0;
	int s = 0;
	int flag = 0;
	vector<int> ans;

	for (int i = 0; i < arr.size(); i++) {
		totSum += arr[i];
		mp[arr[i]] = mp[arr[i]]+1;
	}

	sort(arr.begin(),arr.end());
	int i = N - 1;
	while (i >= 0) {	
		int frq = mp[arr[i]];
		if ((frq + ans.size()) < (N - (frq + ans.size())))
		{
			for (int k = 0; k < frq; k++)
			{
				ans.push_back(arr[i]);
				totSum -= arr[i];
				s += arr[i];
				i--;
			}
		}
		else {
			i -= frq;
		}	
		if (s > totSum) {
			flag = 1;
			break;
		}
	}


	if (flag == 1) {
		for (i = ans.size() - 1; i >= 0; i--) {
			cout<<ans[i]<<" ";
		}
	}
	else {
		cout<<-1;
	}
}

// vi minElements(vi &a) {
//   int halfSum = 0;
//   for (int i=0; i<n; ++i) {
//     halfSum += a[i]
//   }

//   halfSum /= 2;
//   sort(a.begin(), a.end());

//   vi subset;
//   int res = 0;
//   int currSum = 0;

//   for (int i=0; i < n; ++i) {
//     currSum += a[i];
//     subset.push_back(a[i]);
//     res += 1;

//     if (currSum > halfSum) {
//       return subset;
//     }
//   }

//   return subset;
// }

int main()
{
	vector<int> arr = { 3,7,5,6,2 };
	findSubset(arr);
  return 0;
}