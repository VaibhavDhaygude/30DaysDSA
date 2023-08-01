#include<iostream>
using namespace std;

int main(){
    int k;
    int arr[10]={5,3,7,1,8,4,6,2,10,9};
    cout<<"Enter K: "<<endl;
    cin>>k;
    int n=sizeof(arr)/sizeof(arr[0]);
    int temp;
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            if(arr[i]>arr[j]){
                temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }5
        }
    }
    for(int i=0;i<n;i++){
        cout<<arr[i]<<endl;
    }
    cout<<"Kth Largest Number is: "<<arr[k-1];

}