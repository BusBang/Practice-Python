#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct student {
	int number;
	char name[10];
	double grade;
};

int main(void){
	struct student s;
	
	printf("학번을 입력하세요 : ");
	scanf("%d", &s.number);
	printf("이름을 입력하세요 : ");
	scanf("%s", s.name);	// 배열은 그 자체로 주소값을 갖고 있기 때문에 &가 필요 없음
	printf("학점을 입력하세요 : ");
	scanf("%lf", &s.grade);
	 
	
	
	printf("학번 : %d\n", s.number);
	printf("이름 : %s\n", s.name);
	printf("학점 : %1.f\n", s.grade);
	return 0;
}
