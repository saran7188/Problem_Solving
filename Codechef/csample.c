#include<stdio.h>
#include<stdlib.h>

void call(int **,int *,int *);

int main(){
    int m,n;
    scanf("%d%d",&m,&n);
    int **ptr;
    ptr = (int **)malloc(sizeof(int *)*n);
    for (int i=0;i<m;i++){
        ptr[i]=(int *)malloc((sizeof(int))*m);
    }
    for (int i=0;i<m;i++){
        for (int j=0;j<n;j++){
            scanf("%d",(*(ptr+i)+j));
        }
    }
    call(ptr,&m,&n);
}

void call(int **s,int *m,int *n){
    for (int i=0;i<*m;i++){
        for(int j=0;j<*n;j++){
            printf("%d ",*(*(s+i)+j));
        }printf("\n");
    }
}