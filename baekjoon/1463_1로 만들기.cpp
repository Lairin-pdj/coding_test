#include <iostream>
#include <algorithm>

using namespace std;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int a;
    cin >> a;
    
    int ans[1000001] = {0, };
    ans[1] = 0;
    
    for(int i = 2; i <= a; i++){
        ans[i] = ans[i - 1] + 1;
        if(i % 2 == 0)
            ans[i] = min(ans[i], ans[i / 2] + 1);
        if(i % 3 == 0)
            ans[i] = min(ans[i], ans[i / 3] + 1);
    }
    
    cout << ans[a];
    
    return 0;
}
