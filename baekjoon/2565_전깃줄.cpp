#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, a, b;
    cin >> n;
    vector<pair<int, int>> vec;
    for(int i = 0; i < n; i++){
        cin >> a >> b;
        vec.push_back(make_pair(a, b));
    }
    
    sort(vec.begin(), vec.end());
    
    int d[n + 1] = {0, };
    d[0] = 1;
    int answer = 0;
    for (int i = 1; i < n; i++) {
        int temp = 0;
		for (int j = 0; j < i; j++) {
			if (vec[j].second < vec[i].second) {
			    temp = max(temp, d[j]);
			}
		}
		d[i] = temp + 1;
		answer = max(answer, d[i]);
    }
    
    cout << n - answer << "\n";
    
    return 0;
}
