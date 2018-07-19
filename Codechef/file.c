#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct{
    int roll_no;
    char name[100];
    char grade[20];
}stud;

int main(){
	stud a;
	FILE *ptr;
	ptr=fopen("k.txt","wb");
	scanf("%d %s %d",&a.roll_no,a.name,a.grade);
	fwrite(&a,sizeof(stud),1,ptr);
	fclose(ptr);
}