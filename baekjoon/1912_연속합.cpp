#include <iostream>
#include <algorithm>

using namespace std;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    int a[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    
    int sum[n] = {0, };
    int answer = a[0];
    sum[0] = a[0];
    for(int i = 1; i < n; i++){
        sum[i] = max(sum[i - 1] + a[i], a[i]);
        answer = max(answer, sum[i]);
    }

    cout << answer;
    
    return 0;
}
