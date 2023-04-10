#include <iostream>
#include <cmath>

using namespace std;

int gcd(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
}

int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    int n = 1;
    for (int i = 2; i <= 20; i++) {
        n = lcm(n, i);
    }
    cout << "The smallest number which can be divided by numbers from 1 to 10 without any remainder is: " << n << endl;
    return 0;
}