/*Consider an -element array, , where each index  in the array contains a reference to an array of  integers (where the value of  varies from array to array). See the Explanation section below for a diagram.

Given , you must answer  queries. Each query is in the format i j, where  denotes an index in array  and  denotes an index in the array located at . For each query, find and print the value of element  in the array at location  on a new line.*/
//hackarrank vector program 
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
/*
2 2
3 1 5 4
5 1 2 8 9 3
0 1
1 3
*/
/*
5
9
*/

int main() {
    int n,q,k,i,j,x,y;
    scanf("%d %d",&n,&q);
    vector<int> a[n];
    for(i=0;i<n;i++)
    {
      scanf("%d",&k);
      int o;
      for(j=0;j<k;j++)
      {
        scanf("%d",&o);
        a[i].push_back(o);
      }
    }
    for(int l=0;l<q;l++)
    {
        scanf("%d %d",&x,&y);
        printf("%d\n",a[x][y]);
    }
    return 0;
}
