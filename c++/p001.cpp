#include <iostream>
using namespace std;

int sumMultiples(int a, int b, int slim){
    int sum_ab = 0;
    for (int i=1;i<slim;i++){
        if(i % a == 0 || i % b == 0){
            sum_ab +=i;
        }
    }
    return sum_ab;
}
int main()
{
    cout << sumMultiples(3,5,10);
    return 0;
}
