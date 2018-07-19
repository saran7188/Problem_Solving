#include<stdio.h>
#include<stdlib.h>


typedef struct{
    int roll_no;
    char name[100];
    char grade;
}stud;

void lala(stud *a);

int main(){
	stud a;
	scanf("%d %s %c",&a.roll_no,a.name,&a.grade);
	lala(&a);
}

void lala(stud *a){
	printf("%d %s %c\n",(a->roll_no),(a->name),(a->grade));
}