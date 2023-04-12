#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int bruteforce(int n){
    int sum = 0;
    int square_sum = 0;
    for (int i = 0; i <= n; i++){
        sum += i;
        square_sum += i * i;
    }
    return sum*sum - square_sum;
}

int compute(int n){
    int sum_of_squares = 0,squares_of_sum = 0;
    
    sum_of_squares = n*(n + 1)/2;
    sum_of_squares= pow(sum_of_squares,2);

    squares_of_sum = n*(n+1)*(2*n+1) /6;
   
    return sum_of_squares - squares_of_sum;
}


int main(){
    cout << "Project Euler 6"<<endl;
    cout << bruteforce(100) << endl;
    cout << compute(100) << endl;
    return 0;
}