// 参考代码
#include<bits/stdc++.h>
using namespace std;

int n,t;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0),cout.tie(0);
    	cin>>n>>t;
	vector<int> v(n+10,0);
	vector<bool> st(n+10,false);
	for(int i=1;i<n;i++)
		cin>>v[i];
	int idx=1;
	while(n-1){
		idx=idx+v[idx];
		if(st[idx]){
			cout<<"NO";
			return 0;
		}
		if(idx==t){
			cout<<"YES";
			return 0;
		}else{
			st[idx]=true;
			n--;
		}
	}
	cout<<"NO";
    return 0;
}