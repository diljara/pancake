#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

void print(int numbers[4][4])
{
for (int i=0; i < 4; i++, cout << endl)
{
    for (int j=0; j < 4; j++)
    {
    cout << numbers[i][j];
}
}
cout << endl;
}
void step(int numbers[4][4], int ** empti)
{
}
int main()
{
int numbers [4][4] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
print(numbers);
srand(time(NULL));
int n = rand() % 4;
int empti [4][2] = {};
for (int i=0; i < n; i++)
{
int x = rand() % 4;
int y = rand() % 4;
empti[i][0] = x;
empti[i][1] = y;
numbers[x][y] = 0;
}
print(numbers);


}
