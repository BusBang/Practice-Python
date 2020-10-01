#include <stdio.h>
// io의 std라는 것. 
// scanf : i 명령어

int main(void) {
	int x;
	
	printf("아무 숫자나 눌러주세요. ");
	scanf("%d", &x);
	printf("아무 숫자 : %d", x);

//	& : 메모리값을 지정해주는 것 
	return 0;
	
} 
