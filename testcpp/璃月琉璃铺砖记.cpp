// 参考代码
#include<bits/stdc++.h>
using namespace std;

void solve(){
	int m,n;
	cin>>m>>n;
	cout<<max(m/2*n+(m%2)*(n/2),n/2*m+(n%2)*(m/2));
}

int main() {
    // ios::sync_with_stdio(0);
    // cin.tie(0),cout.tie(0);
    int t=1;
    while(t--){
        solve();
    }
    return 0;
}