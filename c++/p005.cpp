#include <iostream>
#include <vector>
#include <set>
#include <cmath>
using namespace std;
vector<int> prime_factorization(int n) {
    vector<int> prime_factors;
    int c = 2; 
    prime_factors.push_back(c);
    while (n>1){
        if (n % c == 0){
            n = n / c;
            prime_factors.push_back(c);
        }
        else{
            c = c + 1;
        }
    }
    return prime_factors;   
}
vector<int> lcm(vector<int> nlist) {
    set<int> primes;
    for (size_t i = 0; i < nlist.size(); ++i) {
        vector<int> n = prime_factorization(nlist[i]);
        for (size_t j = 0; j < n.size(); ++j) {
            primes.insert(n[j]);
            }
        }
    vector<int>ans(primes.begin(),primes.end());
    return ans;
}

int compute(int k, vector<int>& p) {
    int N=1, i=0;
    bool check = true;
    double lim = sqrt(k);
    vector<int> a(p.size(),0);
    while (p[i] < k){
        a[i] = 1;
        if (check){
            if (p[i] <= lim){
                a[i] = floor(log(k) / log(p[i]));
            }
            else{
                check = false;
            }
        }
        N = N * pow(p[i],a[i]);
        i = i + 1;
        if(i==p.size()){
            break;
        }
    }
    return N;
}

int main() {
    vector<int> nlist;
    for (int i = 2; i <= 20; ++i) {
        nlist.push_back(i);
    }
    vector<int> factors = lcm(nlist);
    for (int i = 0; i < factors.size(); i++){
        cout<<factors[i]<<' ';
    }
    cout << '\n';
    int ans = compute(20,factors);
    cout << ans << endl;
    return 0;
}