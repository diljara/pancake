#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

void print(int numbers[10][10])
{
    for (int i=0; i < 10; i++, cout << endl)
    {
        for (int j=0; j < 10; j++)
        {
            cout << numbers[i][j];
        }
    }
    cout << endl;
}




void step(int numbers[10][10], int empti[10][2], int n)
{

    for (int i = 0; i < n; i++)
    {
        int x = empti[i][0];
        int y = empti[i][1];
        if (numbers[x][y] == 0)
        {
            int z = rand() % 4;
            if (z == 0) {
                empti[i][0]++;
            }
            if (z == 2) {
                empti[i][0]--;
            }
            if (z == 1) {
                empti[i][1]++;
            }
            if (z == 3) {
                empti[i][1]--;
            }

            numbers[x][y] = 1;
            numbers[empti[i][0]][empti[i][1]] = 0;
        }
    }
}



void check(int numbers[10][10], int empti[10][2], int n)
{
    for (int i = 0; i < n; i++)
    {
        int x = empti[i][0];
        int y = empti[i][1];
        if ((x == 10 - 1) || (y == 10 - 1) || (x == 0) || (y == 0)){
               numbers[x][y] = -1;
            }
        else {
             for (int j = i + 1; j < n; j++)
               {
                 if (abs(x - empti[j][0]) + abs (y - empti[j][1]) == 1)
                  {
                   numbers[x][y] = -1;
                   numbers[empti[j][0]][empti[j][1]] = -1;

                    }

                }
            }
    }
}


int multiply(int numbers[10][10])
{
    int s = 1;
    for (int i = 0; i < 10; i++)
    {
       for (int j = 0; j < 10; j++)
        {
            s = s * numbers[i][j];
        }
    }
    return s;
}



int main()
{
    int len = 10;
    int numbers[10][10] = { 0 };
    for (int i=0; i < 10; i++)
    {
        for (int j=0; j < 10; j++)
            {
            numbers[i][j] = 1;
            }
    }
    //print(numbers);
    srand(time(NULL));
    int n = rand() % 10;
    int empti [10][2];
    for (int i=0; i < n; i++)
    {
        int x = rand() % 10;
        int y = rand() % 10;
        empti[i][0] = x;
        empti[i][1] = y;
        numbers[x][y] = 0;
    }
    //print(numbers);
    //for (int i=0; i < n; i++, cout << endl)
    //{
        //for (int j=0; j < 2; j++)
        //{
        //cout << empti[i][j];
        //}
    //}
    bool done = true;
    cout << 0 << endl;
    print(numbers);
    check(numbers, empti, n);
    for (int t = 1; done == true; t++)
    {
        step(numbers, empti, n);
        check(numbers, empti, n);
        cout << t << endl;
        print(numbers);
        done = (multiply(numbers) == 0);
    }


    return 0;
}


void check(int numbers[6][6], int empti[6][2], int n)
{
    for (int i=0; i < n; i++)
    {
        int x = empti[i][0];
        int y = empti[i][1];
        if ((x == 5) || (y == 5) || (x == 0) || (y == 0)){
               numbers[x][y] = -1;
            }
        else {
             for (int j = i + 1; j < n; j++)
               {
                 if (abs(x - empti[j][0]) + abs (y - empti[j][1]) == 1)
                  {
                   numbers[x][y] = -1;
                   numbers[empti[j][0]][empti[j][1]] = -1;

               }

        }
        }
    }
}


int multiply(int numbers[6][6])
{
    int s = 1;
    for (int i = 0; i < 6; i++)
    {
       for (int j = 0; j < 6; j++)
        {
            s = s * numbers[i][j];
        }


    }
    return s;
}



int main()
{
    int len = 6;
    int numbers[6][6] = { 0 };
    for (int i=0; i < 6; i++)
    {
        for (int j=0; j < 6; j++)
            {
            numbers[i][j] = 1;
            }
    }
    //print(numbers);
    srand(time(NULL));
    int n = rand() % 6;
    int empti [6][2];
    for (int i=0; i < n; i++)
    {
        int x = rand() % 6;
        int y = rand() % 6;
        empti[i][0] = x;
        empti[i][1] = y;
        numbers[x][y] = 0;
    }
    //print(numbers);
    for (int i=0; i < n; i++, cout << endl)
    {
        for (int j=0; j < 2; j++)
        {
        //cout << empti[i][j];
        }
    }
    bool done = true;
    cout << 0 << endl;
    print(numbers);
    check(numbers, empti, n);
    for (int t = 1; done == true; t++)
    {
        done = (multiply(numbers) == 0);
        step(numbers, empti, n);
        check(numbers, empti, n);
        cout << t << endl;
        print(numbers);
        done = (multiply(numbers) == 0);
    }


    return 0;
}
