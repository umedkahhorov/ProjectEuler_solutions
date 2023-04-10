#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;
bool check_palindromic(int n){
    string s = to_string(n);
    string s_r = string(s.rbegin(),s.rend());
    if (s==s_r){
        return true;    
    }
    else{
        return false;
    }
}
int palindromic_number(){
    int nmax = 0;
    for (int i = 999; i >=100; i--){
        if (i*i <nmax){
            break;
        }
        for (int j = i; j>=100 ; j--){
            int c = i * j;
            bool is_palindromic = check_palindromic(c);
            if (is_palindromic == true){
                if (c>nmax){
                    nmax = c;
                }
                break;
            }
        }
    }
    return nmax;
}
int main(int argc, char** argv){

    cout << "Project Euler 4" << endl;
    cout << palindromic_number()<<endl;
    return 0;
}
