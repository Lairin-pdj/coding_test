#include <iostream>

using namespace std;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int mem[101][101][101] = {0, };
    mem[1][1][1] = 1;
    
    int N, L, R;
    cin >> N >> L >> R;
    
    for(int i = 2; i < N + 1; i++){
        for(int j = 1; j < L + 1; j++){
            for(int k = 1; k < R + 1; k++){
                mem[i][j][k] = (mem[i - 1][j - 1][k] + mem[i - 1][j][k - 1] + (long long)mem[i - 1][j][k] * (i - 2)) % 1000000007;
            }
        }
    }
    
    cout << mem[N][L][R] << "\n";
    
    return 0;
}
