#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void call(int *,int );

int main(){
	int n;
	scanf("%d",&n);
	int a[n];
	for (int i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	call(a,n);
	for(int i=0;i<n;i++){
		printf("%d ",*(a+i));
	}printf("\n");
}

void call(int *a,int n){
	for(int i=0;i<n;i++){
		printf("%d ",*(a+i));
		*(a+i)+=1;
	}printf("\n");
}