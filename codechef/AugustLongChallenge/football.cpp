#include <bits/stdc++.h>

using namespace std; 

int main() {
    int T, N, tmp;
    int max, score; 
    
    cin >> T;
    for(int i = 0; i < T; i++) {
        vector<int> A, B;
        cin >> N;    
        
        for (int j = 0; j < N; j++) {
            cin >> tmp; 
            A.push_back(tmp);
        }

        for (int j = 0; j < N; j++) {
            cin >> tmp; 
            score = (A[j] * 20) - (tmp * 10);

            if (score > 0 && score > max) {
                max = score;
            }
        }

        cout<<max<<"\n";
        max = 0;
    }

    return 0;
}
