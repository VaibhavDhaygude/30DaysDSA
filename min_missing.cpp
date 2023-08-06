#include<iostream>
using namespace std;

int cal(int arr[],int n){
    int min=1;
    for(int i=0;i<n;i++){
        if(arr[i]==min+1){
            min=arr[i];
            
        }
    }
    return min+1;

}

int main(){
    int arr[]={1,2,3,4,5};
    cout<<cal(arr,sizeof(arr)/sizeof(arr[0]));


}