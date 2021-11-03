#include <iostream>
#include <algorithm>

using namespace std;

int main(void){
    // 입력속도 최적화
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int a;
    cin >> a;
    int b[3];
    int c[3];
    
    // 초기값 설정
    cin >> c[0] >> c[1] >> c[2];
    
    // 반복적으로 입력 받으면서 동적계획
    for(int i = 0; i < a - 1; i++){
        int temp[3];
        cin >> b[0] >> b[1] >> b[2];
        temp[0] = min(b[0] + c[1], b[0] + c[2]);
        temp[1] = min(b[1] + c[0], b[1] + c[2]);
        temp[2] = min(b[2] + c[0], b[2] + c[1]);
        c[0] = temp[0];
        c[1] = temp[1];
        c[2] = temp[2];
    }
    int answer = min(c[0], min(c[1], c[2]));
    
    cout << answer << "\n";
    
    return 0;
}
