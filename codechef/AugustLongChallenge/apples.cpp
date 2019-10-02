#include <bits/stdc++.h> 

using namespace std; 

int main() {
    int t; 
    cin >> t; 
    string yes = "YES", no = "NO";

    for (int i = 0; i < t; i++) {
      unsigned long n, k, distribution; 
      cin >> n >> k; 

      distribution = n / k; 
      if (distribution % k == 0) {
        cout << no <<"\n";  
      } else {
        cout << yes << "\n"; 
      }
    }

    return 0; 
}
