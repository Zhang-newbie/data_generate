// 参考代码
#include<bits/stdc++.h>
using namespace std;

int a,b,c;
typedef long long LL;

bool check(LL x){
	LL sum=x*b;
	for(int i=1;i<=c;i++){
		sum+=b;
		sum-=a;
		if(sum<0){
			return false;
		}
	}
	return true;
}

void solve(){
	cin>>a>>b>>c;
	LL l=0,r=1e10,mid;
	while(l<r){
		mid=(l+r)/2;
		if(check(mid)){
			r=mid;
		}else{
			l=mid+1;
		}
	}
	cout<<l;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0),cout.tie(0);
    int t=1;
    while(t--){
        solve();
    }
    return 0;
}