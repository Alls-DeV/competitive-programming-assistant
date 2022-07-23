#include <bits/stdc++.h>

#ifdef ALE
	#include "/home/alls/Library/debug.h"
#else
	#define dbg(...)
#endif
 
using namespace std;

using vi = vector<int>; using vvi = vector<vi>;
using ll = long long; using vll = vector<ll>; using vvll = vector<vll>;
using pi = pair<int, int>; using vpi = vector<pi>;
using pll = pair<ll, ll>; using vpll = vector<pll>;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define rFOR(i, a, b) for (int i = (a); i >= (b); --i)
 
#define SZ(x) (int)(x).size()
#define ALL(x) x.begin(), x.end()
#define PB push_back
#define MP make_pair
#define MU(x) {sort(ALL(x)); x.erase(unique(ALL(x)), x.end());}
#define F first
#define S second

#define uid(a, b) uniform_int_distribution<int>(a, b)(rng) 
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

const int MOD = 1000000007;
const long double eps = 5e-8;
const char nl = '\n';
 
///////////////////////////////////////////////////////////////////////////
//////////////////// DO NOT TOUCH BEFORE THIS LINE ////////////////////////
///////////////////////////////////////////////////////////////////////////
 
void solve() {
}
 
int32_t main() {
    cin.tie(0)->sync_with_stdio(0);

    int t = 1;
	cin >> t;//testcase
    while (t--) {
        #ifdef ALE
			cout << "\033[1;31m" << "------------------------------\n" << "\033[0m";
        #endif
        solve();
    }
}
