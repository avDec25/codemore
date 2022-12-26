#include <iostream>
using namespace std;
int knapSack(int w, int* wt, int* val, int n)
{
    int t[n + 1][w + 1];

    // Initialize matrix
    for (int i = 0; i < w + 1; i++)
        t[0][i] = 0;
    for (int j = 0; j < n + 1; j++)
        t[j][0] = 0;

    // Choice Diagram to code
    for (int i = 1; i < n + 1; i++)
    {
        for (int j = 1; j < w + 1; j++)
        {
            // 1. In case of choice
            if (wt[i - 1] <= j)
            {
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], 0 + t[i - 1][j]);
            }
            // 2. No choice
            else if (wt[i - 1] > j)
            {
                t[i][j] = 0 + t[i - 1][j];
            }
        }
    }
    return t[n][w];
}

int main()
{
    int N = 3;
    int W = 4;
    int values[] = {1, 2, 3};
    int weight[] = {4, 5, 1};
    cout << knapSack(W, weight, values, N);
    cout << "====================";
    return 0;
}