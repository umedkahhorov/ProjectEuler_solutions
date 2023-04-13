#include <iostream>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

bool prime_factorization(int n){
    vector<int> prime_factors;
    int c = 2;
    while (n>1){
        if (n % c == 0){
            n = n / c;
            prime_factors.push_back(c);
        }
        else{
            c = c +1;
        }
    }
    if (prime_factors.size()==1){
        return true;
    }
    else{
        return false;
    }
}

int check_primes(int m){
    int n = 2 , i = 0;
    vector<int> primes;
    while(i<m){
        if(prime_factorization(n)){
            primes.push_back(n);
            i = i + 1;
            n = n + 1;
        }
        else{
            n = n + 1;
        }
    }
    return primes[primes.size() - 1];
}

bool isPrime(int n){
    if (n==1){
        return false;
    }
    if (n<4){
        return true;
    }
    if (n<9){
        return true;
    }
    if(n % 3 == 0){
        return false;
    }
    else{
        int r = floor(sqrt(n)); // sqrt(n); r * r <=n
        int f = 5;
        while (f<=r){
            if(n % f == 0){
                return false;
            }
            if(n % (f+2) ==0){
                return false;
            }
            f = f + 6;
        }
    }
    return true;
}

int main(){
    //vector<int> ans = check_primes(6);
    //for (size_t i = 0; i < ans.size(); ++i) {
    //    cout << "n[" << i << "] = " << ans[i] << endl;
    // }
    int nlim = 10001;
    int count = 1;
    int candidate = 1;

    do {
        candidate += 2;
        if(isPrime(candidate)){
            count++;
        }
    }while (count!=nlim);
    cout<<candidate<<endl; 
    int ans = check_primes(10001);
    cout << " Problem 7 " << ans << endl;

    return 0;
}