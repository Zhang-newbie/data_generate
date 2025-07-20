#include<bits/stdc++.h>

using namespace std;

const int N = 1020;

int f[N][N];
int n, m;
string s, p;

int main(){
    cin >> s  >> p;
    int n=s.size(),m=p.size();
    s = ' ' + s, p = ' ' + p;
    // memset(f, 0x3f, sizeof f);
    // if(s[1] != p[1]) f[1][1] = 1;
    // else f[1][1] = 0;
    for (int i = 0; i <= m; i ++ ) f[0][i] = i;
    for (int i = 0; i <= n; i ++ ) f[i][0] = i;
    for(int i = 1; i <= n; ++i){
        for(int j = 1; j <= m; ++j){
            if(s[i] == p[j]) f[i][j] = min(min(f[i - 1][j], f[i][j - 1])+ 1, f[i - 1][j - 1]);

            else f[i][j] = min(f[i - 1][j], min(f[i][j - 1], f[i - 1][j - 1])) + 1;
        }
    }
    cout << f[n][m] << endl;
    return 0;
}