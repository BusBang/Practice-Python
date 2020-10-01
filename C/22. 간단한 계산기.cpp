#include <stdio.h>

//간단한 계산기 만들기
//getchar(); 


int main(void) {
	char o;
	int x, y;
	while(1) {
		printf("수식을 입력하세요 : ");
		scanf("%d %c %d", &x, &o, &y);
		if(o == '+') {
			printf("%d %c %d = %d\n", x, o, y, x+y); 
		}else if(o == '-'){
			printf("%d %c %d = %d\n", x, o, y, x-y); 
		}else if(o== '*'){
			printf("%d %c %d = %d\n", x, o, y, x*y); 
		}else if(o == '%'){
			printf("%d %c %d = %d\n", x, o, y, x%y); 
		}else {
			printf("잘못된 값을 입력했습니다. "); 
		}
		getchar(); // 엔터를 처리함 
		printf("프로그램을 종료하시겠습니까? (y/n) ");
		scanf("%c", &o);
		if(o == 'n' || o =='N') {
			continue;
		}else if(o == 'y' || o =='Y') {
			break;
		}else {
			printf("잘못 입력하였습니다. \n");
		}
		
		
	}
	
}
