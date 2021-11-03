#include <iostream>
#include <algorithm>

using namespace std;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int a;
    cin >> a;
    int s[a + 1];
    for(int i = 1; i < a + 1; i++){
        cin >> s[i];
    }
    
    int ans[a + 1];
    ans[0] = 0;
    ans[1] = s[1];
    ans[2] = ans[1] + s[2];
    for(int i = 3; i < a + 1; i++){
        ans[i] = max(ans[i - 2] + s[i], ans[i - 3] + s[i - 1] + s[i]);
    }
    
    cout << ans[a] << "\n";
    
    return 0;
}
