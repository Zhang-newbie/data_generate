// 参考代码
#include<bits/stdc++.h>
using namespace std;

const int N=1010;


struct Da{
    int step,x,y;
};
int n,g[N][N];
int dx[]={-1,0,1,0},dy[]={0,1,0,-1};


int bfs(){
    queue<Da> q;
    q.push({0,1,1});
    g[1][1] = 1;
    while(q.size()){
        Da t=q.front();
        q.pop();
        if(t.x==n&&t.y==n) 
            return t.step;
        for(int i=0;i<4;i++){
            int tx=t.x+dx[i],ty=t.y+dy[i];
            if(tx<1||tx>n||ty<1||ty>n||g[tx][ty]==1) 
                continue;
            q.push({t.step + 1,tx,ty});
            g[tx][ty]=1;
        }
        
    }

    return -1;
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0),cout.tie(0);
    cin>>n;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++)
            cin>>g[i][j];
    }
    cout<<bfs();
    return 0;
}