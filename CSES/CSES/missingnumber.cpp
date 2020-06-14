#include <bits/stdc++.h>
using namespace std;

int main(void){
    long long int n,k,i,flag=0,l=0,j;
    cin>>n;
    k=((n)*(n+1))/2;
    for(i=0;i<n-1;i++){
        cin>>j;
        l=l+j;
    }
    cout<<k-l;
}