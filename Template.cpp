#include <bits/stdc++.h>

#ifdef ALE
	#include "/home/alls/Library/debug.h"
#else
	#define dbg(...)
#endif
 
using namespace std;
//#define int long long
using ll = long long;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define rFOR(i, a, b) for (int i = (a); i >= (b); --i)
 
#define ssize(x) (int)(x).size()
#define ALL(x) x.begin(), x.end()
#define rALL(x) x.rbegin(), x.rend()
#define MU(x) {sort(ALL(x)); x.erase(unique(ALL(x)), x.end());}

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
	cin >> t;//remove if single testcase
    while (t--) {
        #ifdef ALE
			cout << "\033[48;5;196m\033[38;5;15m" << "                                     \n" << "\033[0m";
        #endif
        solve();
    }
}
