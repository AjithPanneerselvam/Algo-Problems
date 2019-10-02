#include <bits/stdc++.h> 

using namespace std; 

void swap(string& s, int index) {
    if (s[index] == '1')  {
        s[index] = '0';
    } else if (s[index] == '0'){
        s[index] = '1';
    }
} 

int main() {
    int t; 
    cin >> t; 

    for (int i = 0; i < t; i++) {
        string s; 
        cin >> s; 
        for (int j = 0; j < s.size(); j++) {
            if (s[j] == '1') {
                if (j - 1 >= 0) {
                    swap(s, j-1);
                }
                if (j + 1 < s.size()) {
                    swap(s, j + 1);
                }
                s[j] = '9';
            } 
        }

        int countNines = 0; 
        for (int j = s.size(); j >= 0; j--) {
            if (s[j] == '1') {
                if (j - 1 >= 0) {
                    swap(s, j-1);
                }
                if (j + 1 < s.size()) {
                    swap(s, j + 1);
                }
                s[j] = '9';
                countNines++;
            } else if (s[j] == '9') {
                countNines++;
            } 
        }

        if (countNines == s.size()) {
            cout<<"WIN"<<"\n";
        } else {
            cout<<"LOSE"<<"\n";
        }
    }
    
    return 0; 
}
