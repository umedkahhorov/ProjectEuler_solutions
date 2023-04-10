#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int primefactor(int n){
    vector<int> prime_factors;
    int c = 2; // smallest factor
    prime_factors.push_back(c);
    while (n > 1){
        if(n % c == 0){
            cout << c << endl;
            n = n / c;
            prime_factors.push_back(c); // append only prime factors
        }
        else{
            c = c + 1;
        }
    }
    int maxf = *max_element(prime_factors.begin(),prime_factors.end());
    return maxf;
}

int main(int argc, char** argv){
    if (argc < 2){
        cout << "Usage: " << argv[0] << " <number>" << std::endl;
        return 1;
    }
    u_int64_t n = stoi(argv[1]);
    cout << "Project Euler 3" << endl;
    cout << primefactor(n)<<endl;
    return 0;
}
