#include <iostream>
#include <string>
using namespace std;

int main(void){
    int n;
    cin >> n;
    
    string s, t;
    
    for (int i = 0; i < n; i++) {
        char temp;
        cin >> temp;
        s += temp;
    }
    
    int i = 0;
	int j = n - 1;
 
	while (i <= j) {
		if (s[i] == s[j]) {
			int ti = i + 1;
			int tj = j - 1;
			bool flag = false;
			while (ti <= tj) {
				if (s[ti] < s[tj]) {
					t += s[i++];
					flag = true;
					break;
				}
				else if (s[ti] > s[tj]) {
					t += s[j--];
					flag = true;
					break;
				}
				else {
					ti++;
					tj--;
				}
			}
			if (!flag) {
				t += s[i++];
			}
		}
		else if (s[i] < s[j]) {
			t += s[i++];
		}
		else {
			t += s[j--];
		}
	}
    
    for (int i = 0; i < n; i++) {
        if (i != 0 and i % 80 == 0) {
            cout << endl;
        }
        cout << t[i];
    }
}
