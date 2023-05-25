#include <iostream>
#include <vector>

const int MN = 1001;
using namespace std;

vector<int> g[MN];
bool vst[MN];
void dfs(int n){
    vst[n] = true;
    for(int nxt =0; nxt < g[n].size(); nxt++){
        int i = g[n][nxt];
        if(!vst[i]){
            dfs(i);
        }
    }
}
int main() {
    
    int N,M;
    cin >> N >> M;
    for(int i=0; i<M; i++){
        int u,v; cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    
    int cnt = 0;
    for(int i=1; i<=N; i++){
        if(!vst[i]){
            dfs(i);
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}