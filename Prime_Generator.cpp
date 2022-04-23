#include <bits/stdc++.h>
using namespace std;

bool isprime(int n){
    if(n<2) return false;
    if(n==2) return true;
    if(n%2==0) return false;
    for(int i = 3; i*i <= n ; i += 2){
        if(n%i==0) return false;
    }
    return true;

}

// driver code
int main(){
    long long int t,m,n;
    cin >> t;
    while(t--){
        cin >> m >> n;
        for(int i=m ; i<=n; i++){
            if (isprime(i)){
                cout << i << endl;
            }
        }
        cout << endl;
    }
    return 0;
}