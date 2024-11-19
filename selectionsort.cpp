#include<bits\stdc++.h>
using namespace std;

void swap(int &x,int &y){
    int temp;
    temp=x;
    x=y;
    y=temp;
}
void sort(int arr[],int n){
    for(int i=0;i<=n-2;i++){
        int min_index=i;
        for(int j=i;j<n-1;j++){
            if(arr[j]<arr[min_index]) min_index=j;
        }
        swap(arr[min_index],arr[i]);
    }
}
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    sort(arr,n);
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}