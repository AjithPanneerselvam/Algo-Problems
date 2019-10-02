#include <bits/stdc++.h> 

using namespace std; 

int main() {
    int T; 
    cin >> T; 
    for (int t = 0; t < T; t++) {
        int n; 
        cin >> n;
        vector<int> A(n);
        for (int i = 0; i < n; i++) {
            cin >> A[i];
        }

        long int currentVal = 0; 
        long int triples = 0;
        map<long int, vector<long int> > visited; 
        map<long int, vector<long int> >::iterator it;  

        for (long int i = 0; i < n; i++) {
            long int distance = 0;
            currentVal = currentVal ^ A[i]; 
            if (currentVal == 0) {
                triples += i;
            } 
            
            it = visited.find(currentVal);
            if (it != visited.end()) {
                distance = visited[currentVal][1] + ((visited[currentVal][2] + 1) * (i - visited[currentVal][0]));
                triples += distance - (visited[currentVal][2] + 1); 
                
                visited[currentVal][0] = i; 
                visited[currentVal][1] = distance; 
                visited[currentVal][2] += 1; 
            } else {
                vector<long int> temp;
                temp.push_back(i); 
                temp.push_back(0);
                temp.push_back(0);
                
                visited[currentVal] = temp;
            }
        }

        cout<<triples<<"\n";
    }
}
