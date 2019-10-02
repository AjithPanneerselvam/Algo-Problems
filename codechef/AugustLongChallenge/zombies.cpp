#include <bits/stdc++.h> 

using namespace std; 

int main() {
    int T; 
    cin >> T; 

    for (int t = 0; t < T; t++) {
        int n; 
        cin >> n; 

        vector<unsigned int> radiations(n), health(n), result(n);
        //cout<<"\n"<<radiations.size() << " " << health.size()<<"\n";
        for (int i = 0; i < n; i++) {
                cin >> radiations[i];  
        }
       
        unsigned int tmp;
        for (int i = 0; i < n; i++) {
            //cout<<"\nhealth i "<<i;
            //cin>>tmp;
            //health[i] = tmp;
            cin >> health[i];
            //cout<<"\ngot health "<<i;
        }

        //cout<<"got input"; 
        unsigned int currentRad = 0, temp;
        long int extent;
        map<unsigned int, int> healthMap; 
        for (int i = 0; i < n; i++) {
            temp = currentRad; 

            extent = i + radiations[i]; 
            if (extent < n) {
                result[extent] += 1; 
            }

            currentRad = currentRad - result[i] + 1; 
            result[i] = temp; 
            
            
            map<unsigned int, int>::iterator it = healthMap.find(health[i]); 
            if (it != healthMap.end()) {
                healthMap[health[i]] += 1;  
            } else {
                healthMap[health[i]] = 1;
            }
        }

        currentRad = 0; 
        unsigned int matches = 0; 
        vector<unsigned int> debts(n, 0);
        
        for (int i = n-1; i >= 0; i--) {
            result[i] += currentRad + 1; 

            extent = i - radiations[i]; 
            if (extent > 0) {
                debts[extent] += 1; 
            }

            currentRad = currentRad - debts[i] + 1;  
            map<unsigned int, int>::iterator it = healthMap.find(health[i]); 
            if (it != healthMap.end()) {
                if (healthMap[result[i]] < 1) {
                    break; 
                } else {
                    healthMap[result[i]] -= 1;
                    matches += 1; 
                }
            } else {
                break; 
            }
        }
    
        if (matches == n) {
            cout <<"YES"<<"\n";
        } else {
            cout <<"NO"<<"\n";
        }
    }
    
    return 0; 
}
