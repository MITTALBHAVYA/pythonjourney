#include <iostream>
using namespace std;
void printArr(int arr[], int len)
{
    for (int i = 0; i < len; i++)
    {
        cout << arr[i] << " ";
    }
}
void waveSort(int arr[], int len)
{
    for (int i = 1; i < len; i += 2)
    {
        if (arr[i] > arr[i - 1])
        {
            int temp = arr[i];
            arr[i] = arr[i - 1];
            arr[i - 1] = temp;
        }
        if ((arr[i] > arr[i + 1]) && i <= len - 2)
        {
            int temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
    }
}
int main()
{
    int len;
    cout<<"ENTER THE LENGTH OF ARRAY "<<endl;
    cin>>len;
    int arr[len];
    for(int i=0;i<len;i++)
    {
        printf("ENTER THE %d element of the of the array \n",i+1);
        cin>>arr[i];
    }
    printArr(arr,len);
    waveSort(arr,len);
    printArr(arr,len);
}