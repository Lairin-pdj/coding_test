#include <iostream>

using namespace std;

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    
    int N;
    cin >> N;
    int count = 0;
    int sixCount = 0;
    int num = 666;
    int check = 0;
    int answer = 0;
    
    for(int i = 666; count < N; i++){
        num = i;
        sixCount = 0;
        while(num > 0){
            check = num % 10;
            if(check == 6){
                sixCount++;
            }
            else{
                sixCount = 0;
            }
            if(sixCount >= 3){
                answer = i;
                count++;
                break;
            }
            num /= 10;
        }
    }
    cout << answer << "\n";
}
