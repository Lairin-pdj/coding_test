#include <iostream>
#include <algorithm>

using namespace std;

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n[3];
    while(1){
        cin >> n[0] >> n[1] >> n[2];
        if(n[0] == 0 && n[1] == 0 && n[2] == 0){
            break;
        }
        else{
            sort(n, n + 3);
            if((n[0] * n[0]) + (n[1] * n[1]) == (n[2] * n[2])){
                cout << "right" << "\n";
            }
            else{
                cout << "wrong" << "\n";
            }
        }
    }
}
