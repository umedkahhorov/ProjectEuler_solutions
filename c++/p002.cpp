#include <iostream>
using namespace std;

int sumFibonacci(int n){
    int ans = 0;
    int x = 1;
    int y = 2;
    int i = 0;
    while (i<=n){
        if (i % 2 ==0){
            ans +=x;
        int tempr = x;
        x = y;
        y = tempr;    
        }
    }
    return ans;
}
int main()
{
    cout << sumFibonacci(4000000)<<endl;
    return 0;
}
