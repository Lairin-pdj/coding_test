#include <iostream>
#include <algorithm>

using namespace std;

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int a;
    cin >> a;
    int nums[a];
    
    for(int i = 0; i < a; i++)
        cin >> nums[i];
    
    sort(nums, nums + a);
    
    for(int i = 0; i < a; i++)
        cout << nums[i] << "\n";
    
    return 0;
}
