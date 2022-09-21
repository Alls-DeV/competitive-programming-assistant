#include <bits/stdc++.h>
#ifdef ALE
	#include "/home/alls/Library/debug.h"
#else
	#define dbg(...)
#endif
using namespace std;
//#define int long long
using ll = long long; using vi = vector<int>;
#define ssize(x) (int)(x).size()
#define ALL(x) x.begin(), x.end()
#define rALL(x) x.rbegin(), x.rend()
const char nl = '\n';

void solve() {
}
 
int32_t main() {
    cin.tie(0)->sync_with_stdio(0);
    int t = 1;
	cin >> t;//remove if single testcase
    for (int i = 1; i < t+1; i++) {
        #ifdef ALE
			cout << "\033[48;5;196m" << "                                             \n" << "\033[0m";
        #endif
        //cout << "Case #" << i << ": ";
        solve();
    }
}
