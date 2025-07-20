#include<bits/stdc++.h>
// 睡眠3秒
#include<unistd.h>
using namespace std;
const int N = 5010;
int n,m,k,p,a[N],b[N],ans1,ans2;
signed main(){
    cin>>n>>m>>k>>p;
    for(int i=1;i<=m;i++) cin>>a[i];
    for(int i=1;i<=m;i++) cin>>b[i];
    for(int i=1;i<=m;i++){
		if(p<=ans2){
			cout<<"Star Platinum";
			return 0;
		}
		if(k<=n+ans1){
			cout<<"Killer Queen";
			return 0;
		}
		ans1+=a[i];ans2+=b[i];
	}
	cout<<"Killer Queen";
    return 0;
}